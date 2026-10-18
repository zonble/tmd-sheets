#!/usr/bin/env python3
"""Generate a song Markdown page from a TMD score directory.

Usage:
    python3 scripts/generate_song_markdown.py path/to/4_10_futari_no_heitaisan

Run without a directory to process the current directory.  The directory must
contain one main ``.tmd`` file and may contain a ``*_piano.tmd`` accompaniment.
"""

from __future__ import annotations

import argparse
import html
import re
import subprocess
import sys
from pathlib import Path


TITLE_RE = re.compile(r"^\s*\*\*\s*(.*?)\s*\*\*\s*$")
CREDIT_RE = re.compile(r'^\s*~\s*"(.*?)"\s*$')
BLOCK_COMMENT_RE = re.compile(r"/\*(.*?)\*/", re.DOTALL)


def run(command: list[str], *, cwd: Path | None = None) -> str:
    """Run a command and return stdout, preserving useful diagnostics on error."""
    try:
        result = subprocess.run(
            command,
            cwd=cwd,
            check=True,
            text=True,
            capture_output=True,
        )
    except FileNotFoundError as exc:
        raise RuntimeError(f"找不到外部工具：{command[0]}") from exc
    except subprocess.CalledProcessError as exc:
        detail = (exc.stdout or "") + (exc.stderr or "")
        raise RuntimeError(
            f"指令失敗（{exc.returncode}）：{' '.join(command)}\n{detail.strip()}"
        ) from exc
    return result.stdout


def choose_main_tmd(folder: Path) -> Path:
    candidates = sorted(
        path for path in folder.glob("*.tmd") if not path.name.endswith("_piano.tmd")
    )
    if not candidates:
        raise RuntimeError(f"找不到主 TMD：{folder}")
    if len(candidates) == 1:
        return candidates[0]

    matching = [path for path in candidates if path.stem == folder.name]
    if len(matching) == 1:
        return matching[0]
    names = ", ".join(path.name for path in candidates)
    raise RuntimeError(f"找到多個可能的主 TMD，無法判斷：{names}")


def choose_piano_tmd(folder: Path, main_tmd: Path) -> Path | None:
    candidates = sorted(folder.glob("*_piano.tmd"))
    if not candidates:
        return None
    matching = [path for path in candidates if path.stem == f"{main_tmd.stem}_piano"]
    return matching[0] if matching else candidates[0]


def parse_metadata(text: str) -> tuple[str, list[str]]:
    title = "未命名曲目"
    credits: list[str] = []
    for line in text.splitlines():
        title_match = TITLE_RE.match(line)
        if title_match and title == "未命名曲目":
            title = title_match.group(1)
        credit_match = CREDIT_RE.match(line)
        if credit_match:
            value = credit_match.group(1).strip()
            if re.match(r"^(詞曲|作詞|作曲|編曲|詞：|曲：|詞：|曲：)", value):
                credits.append(value)
    return title, credits


def clean_comment(block: str) -> list[str]:
    lines = []
    for line in block.splitlines():
        line = re.sub(r"^\s*", "", line).rstrip()
        if line.startswith("=") and set(line) <= {"="}:
            continue
        lines.append(line)
    while lines and not lines[0]:
        lines.pop(0)
    while lines and not lines[-1]:
        lines.pop()
    return lines


def extract_notes_and_lyrics(text: str) -> tuple[str, str]:
    comments = [clean_comment(block) for block in BLOCK_COMMENT_RE.findall(text)]
    comments = [[line for line in block if line.strip()] for block in comments]

    note_blocks: list[list[str]] = []
    lyric_blocks: list[list[str]] = []
    for block in comments:
        joined = "\n".join(block)
        if any(marker in joined for marker in ("曲目說明", "版本說明", "出處註記", "調性與拍號")):
            note_blocks.append(block)
        if any(marker in joined for marker in ("歌詞全文", "原書歌詞", "歌詞")):
            lyric_blocks.append(block)

    note_texts: list[str] = []
    for block in note_blocks:
        trimmed = block[:]
        for index, line in enumerate(trimmed):
            if "歌詞全文" in line or "原書歌詞" in line:
                trimmed = trimmed[:index]
                break
        if trimmed:
            note_texts.append("\n".join(trimmed))
    notes = "\n\n".join(note_texts)

    if lyric_blocks:
        lyric_lines = lyric_blocks[0]
        start = 0
        for index, line in enumerate(lyric_lines):
            if "歌詞全文" in line or "原書歌詞" in line:
                start = index + 1
                break
        lyric_lines = lyric_lines[start:]
        lyric_lines = [
            line for line in lyric_lines if not re.match(r"^\s*[（(]語譯", line)
        ]
        lyrics = "\n".join(lyric_lines).strip()
    else:
        # Older files often contain only a plain lyric block without a heading.
        lyric_candidates = [
            block
            for block in comments
            if block and not any(marker in "\n".join(block) for marker in ("曲目說明", "版本說明"))
        ]
        lyrics = "\n".join(lyric_candidates[0]).strip() if lyric_candidates else ""

    return notes, lyrics


def render_analysis(main_tmd: Path, folder: Path) -> str:
    return run(["tmd", "inspect", str(main_tmd), "--locale", "zh-Hant"], cwd=folder)


def generate(
    folder: Path,
    keep_wav: bool = False,
    soundfont: Path | None = None,
) -> Path:
    folder = folder.resolve()
    if not folder.is_dir():
        raise RuntimeError(f"不是資料夾：{folder}")

    main_tmd = choose_main_tmd(folder)
    piano_tmd = choose_piano_tmd(folder, main_tmd)
    title, credits = parse_metadata(main_tmd.read_text(encoding="utf-8"))
    notes, lyrics = extract_notes_and_lyrics(main_tmd.read_text(encoding="utf-8"))

    stem = main_tmd.stem
    abc_path = folder / f"{stem}.abc"
    mp3_path = folder / f"{stem}.mp3"
    wav_path = folder / f"{stem}.wav"
    markdown_path = folder / f"{stem}.md"

    run(["tmd", str(main_tmd), "-a", str(abc_path)], cwd=folder)
    analysis = render_analysis(main_tmd, folder)

    audio_html = "*找不到鋼琴伴奏版 TMD，未產生音訊。*"
    if piano_tmd:
        render_command = ["tmd", str(piano_tmd), "-w", str(wav_path)]
        if soundfont:
            render_command.extend(["--soundfont", str(soundfont.resolve())])
        run(render_command, cwd=folder)
        run(
            [
                "ffmpeg",
                "-y",
                "-i",
                str(wav_path),
                "-codec:a",
                "libmp3lame",
                "-q:a",
                "2",
                str(mp3_path),
            ],
            cwd=folder,
        )
        audio_html = f'<audio controls src="{html.escape(mp3_path.name)}"></audio>'
        if not keep_wav:
            wav_path.unlink(missing_ok=True)

    credits_block = "\n".join(f"- {credit}" for credit in credits) or "- 詞曲作者：未在 TMD metadata 中提供"
    notes_block = notes or "（TMD 檔案未包含額外 note）"
    lyrics_block = lyrics or "（TMD 檔案未包含歌詞註解）"
    abc = abc_path.read_text(encoding="utf-8")

    markdown = f"""# {title}

{audio_html}

{credits_block}

- note

{notes_block}

## 歌詞

```text
{lyrics_block}
```

## 調性分析

```text
{analysis.rstrip()}
```

## ABC

```abc
{abc.rstrip()}
```

- [原始 TMD 檔案]({main_tmd.name})
"""
    markdown_path.write_text(markdown, encoding="utf-8")
    return markdown_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", nargs="?", type=Path, default=Path.cwd())
    parser.add_argument("--keep-wav", action="store_true", help="保留中間 WAV 檔")
    parser.add_argument(
        "--soundfont",
        type=Path,
        help="傳給 tmd -w 的 SoundFont（.sf2/.dls）路徑",
    )
    args = parser.parse_args()
    try:
        output = generate(
            args.directory,
            keep_wav=args.keep_wav,
            soundfont=args.soundfont,
        )
    except RuntimeError as exc:
        print(f"錯誤：{exc}", file=sys.stderr)
        return 1
    print(f"已產生：{output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
