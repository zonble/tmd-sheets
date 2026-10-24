---
name: goahi
description: >-
  Create, edit, explain, and validate traditional Taiwanese opera and Chinese
  theatrical percussion scores in TMD, especially opening drum patterns such as
  長錘、奪頭、鳳點頭 and their transitions. Use for work grounded in the
  /Users/zonble/Work/tmd-sheets/goahi score collection; do not use for generic
  TMD questions without a traditional-theatre scoring context.
---

# Goahi 戲曲鑼鼓樂譜

This skill supplements the general `tmd` skill with the conventions of the
Goahi collection. Read the general TMD skill first whenever syntax, parsing,
measure validation, MIDI, or export behavior is involved.

## Working conventions

- Treat the existing `.tmd` files in this directory as the local style
  reference. Inspect nearby scores before adding a new one so title, metadata,
  track naming, comments, and playback order remain consistent.
- Preserve the collection's numbered-notation approach and use explicit
  percussion tracks when a pattern needs playback or rendering. If a sound
  cannot be represented faithfully by the available TMD instrument or drum
  mapping, keep the musical pattern readable in comments and state the
  approximation instead of silently inventing a notation.
- Represent repeated, freely extendable passages as named sections and put
  their performance order in the final `-> ... ->#` arrangement. Keep an
  ending cue or transition separate when it is useful for reuse.
- Validate every changed or newly created score with the available TMD checker;
  resolve measure-length and execution-order errors before handing it off.
- For traditional-theatre terminology, use the reference below. Distinguish
  the musical function from a literal syllable transcription: the same name
  can have regional, genre, or troupe-specific variants.

## Long hammer and duotou

When the request concerns `長錘`/`長打`, `奪頭`/`垛頭`, or `長錘轉奪頭`, read
[references/theatrical-percussion.md](references/theatrical-percussion.md).
Use it to choose a sensible section structure, explain the dramatic function,
and make assumptions visible. In particular:

- `長錘` is an extendable opening/action pattern whose core spoken mnemonic is
  `倉 七 台 七`.
- `奪頭` is a short, punctuated closing/opening cue that commonly follows a
  long hammer and hands off to the singer or melodic accompaniment.
- `慢長錘`, `快長錘`, and `散長錘` are performance variants; do not collapse
  them into one fixed tempo or claim that one notation fits every regional
  tradition.

## Deliverables

For a new score, provide a valid `.tmd` file and, when useful, a short comment
or companion note identifying the mnemonic, intended use, tempo character, and
any instrument-mapping approximation. For an explanation-only request, give
the traditional meaning first and map it to TMD only if the user asks for a
score or implementation.
