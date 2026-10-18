# TMD Sheets

以 **TMD (Timebase Mark Down)** 語法編寫的樂譜、編曲與實驗作品集。

---

## 目錄結構總覽

```text
tmd-sheets/
├── zonble/             # 個人原創與改編作品集
├── youth-army/         # 青年遠征軍／新一軍軍歌與進行曲組曲
├── kogakko_shoka/      # 日治時期《公學校唱歌》教材數位化與改編
├── uebung/             # 練習曲、音域實驗與演算法卡農生成
└── golden_case/        # TMD 全語法展示與極限壓力測試曲
```

---

## 1. 個人原創與改編作品集 (`zonble/`)

### 交響與大型組曲
* **[`zongzhi_1945/`](zonble/zongzhi_1945/) — 《宗治的1945》三樂章交響組曲**
  * 樂章大綱與索引：[`README.md`](zonble/zongzhi_1945/README.md)
  * 完整總譜：
    * 第一樂章〈城〉：[`movement_1_full.tmd`](zonble/zongzhi_1945/movement_1_full.tmd)
    * 第二樂章〈雪〉：[`movement_2_full.tmd`](zonble/zongzhi_1945/movement_2_full.tmd)
    * 第三樂章〈島〉：[`movement_3_full.tmd`](zonble/zongzhi_1945/movement_3_full.tmd)
  * 主題與段落分譜：[`sections/`](zonble/zongzhi_1945/sections/)（共 21 首主題、賦格與變奏段落）
* **[`landing_at_taoyuan/`](zonble/landing_at_taoyuan/) — 《Landing at Taoyuan: Rhapsody for Orchestra》**
  * [`landing_at_taoyuan.tmd`](zonble/landing_at_taoyuan/landing_at_taoyuan.tmd)
* **[`motif/`](zonble/motif/) — 《勇者傳說 / Simple Motif》系列**
  * [`motif.tmd`](zonble/motif/motif.tmd) — Simple Motif（原始動機）
  * [`childhood.tmd`](zonble/motif/childhood.tmd) — 童年約定 - 純真童年
  * [`hero_ondo.tmd`](zonble/motif/hero_ondo.tmd) — 夏日祭典「勇者音頭」
  * [`rpg_variations.tmd`](zonble/motif/rpg_variations.tmd) — 主人公主題六大場景變奏曲
  * [`rpg_suite_with_transitions.tmd`](zonble/motif/rpg_suite_with_transitions.tmd) — 勇者冒險全景交響組曲（含過場音樂）

### 單曲與多版本編曲
* **[`bugs/`](zonble/bugs/) — 《點蟲蟲》**
  * [`bugs.tmd`](zonble/bugs/bugs.tmd)（原版）、[`bugs_chords.tmd`](zonble/bugs/bugs_chords.tmd)（兒歌版）、[`bugs_arpeggio.tmd`](zonble/bugs/bugs_arpeggio.tmd)（琶音前奏版）、[`bugs_marimba.tmd`](zonble/bugs/bugs_marimba.tmd)（長笛與馬林巴配器版）
* **[`cannotwait/`](zonble/cannotwait/) — 《等不及想要看著你長大》**
  * [`cannot_wait.tmd`](zonble/cannotwait/cannot_wait.tmd)（原版）、[`cannot_wait_chamber.tmd`](zonble/cannotwait/cannot_wait_chamber.tmd)（木管與大提琴室內樂版）
* **[`dust/`](zonble/dust/) — 《塵埃》**
  * [`dust.tmd`](zonble/dust/dust.tmd)（原版）、[`dust_folk.tmd`](zonble/dust/dust_folk.tmd)（民謠搖滾吉他音牆版）、[`dust_orchestra.tmd`](zonble/dust/dust_orchestra.tmd)（狂轟濫炸管弦版）
* **[`golden_rain/`](zonble/golden_rain/) — 《金雨樹之歌》**
  * [`golden_rain.tmd`](zonble/golden_rain/golden_rain.tmd)（原版）、[`golden_rain_autumn.tmd`](zonble/golden_rain/golden_rain_autumn.tmd)（秋日台灣欒樹民謠版）、[`golden_rain_october.tmd`](zonble/golden_rain/golden_rain_october.tmd)（十月深秋弦樂厚重版）
* **[`huoxiangji/`](zonble/huoxiangji/) — 《藿香薊》**
  * [`huoxiangji.tmd`](zonble/huoxiangji/huoxiangji.tmd)（原版）、[`huoxiangji_spring.tmd`](zonble/huoxiangji/huoxiangji_spring.tmd)（Spring Chamber 室內樂版）
* **[`kazoo_player/`](zonble/kazoo_player/) — 《Kazoo Player》**
  * [`kazoo_player.tmd`](zonble/kazoo_player/kazoo_player.tmd)（原版）、[`kazoo_player_wall.tmd`](zonble/kazoo_player/kazoo_player_wall.tmd)（銅管轟炸 × 吉他音牆版）
* **[`shanwai/`](zonble/shanwai/) — 《山外的街道上》**
  * [`shanwai.tmd`](zonble/shanwai/shanwai.tmd)（原版）、[`shanwai_flamenco.tmd`](zonble/shanwai/shanwai_flamenco.tmd)（Flamenco 吉他與木箱鼓版）
  * [`archive/`](zonble/shanwai/archive/)：收錄民謠搖滾（`shanwai_folk_rock.tmd`）、拉丁（`shanwai_latin.tmd`）、探戈（`shanwai_tango.tmd`）等實驗編曲版本
* **[`shinagawa_station/`](zonble/shinagawa_station/) — 《品川車站》**
  * [`shinagawa-station.tmd`](zonble/shinagawa_station/shinagawa-station.tmd)（原版）、[`shinagawa-station-full.tmd`](zonble/shinagawa_station/shinagawa-station-full.tmd)（變奏曲）、[`shinagawa-station-dialogue.tmd`](zonble/shinagawa_station/shinagawa-station-dialogue.tmd)（Call & Response）、[`shinagawa-two-trains.tmd`](zonble/shinagawa_station/shinagawa-two-trains.tmd)（雙車交會）、[`shinagawa-concourse-echoes.tmd`](zonble/shinagawa_station/shinagawa-concourse-echoes.tmd)（人潮、迴音與雙車交會）
* **[`swing/`](zonble/swing/) — 《鐘擺》**
  * [`swing_folk.tmd`](zonble/swing/swing_folk.tmd)（民謠版）、[`swing_postrock.tmd`](zonble/swing/swing_postrock.tmd)（後搖滾音牆版）
* **[`thousands/`](zonble/thousands/) — 《千千萬萬》**
  * [`thousands.tmd`](zonble/thousands/thousands.tmd)（原版）、[`thousands_orchestra_snare.tmd`](zonble/thousands/thousands_orchestra_snare.tmd)（副歌行軍軍鼓版）

---

## 2. 青年軍與新一軍歷史軍歌 (`youth-army/`)

* [`youth_force_march.tmd`](youth-army/youth_force_march.tmd) — 《青年軍進行曲》（洪波 曲）
* [`youth_expeditionary_force_march.tmd`](youth-army/youth_expeditionary_force_march.tmd) — 《青年遠征軍進行曲》（胡然 曲）
* [`new_warriors.tmd`](youth-army/new_warriors.tmd) — 《新戰士進行曲》（胡然 曲）
* [`201.tmd`](youth-army/201.tmd) — 《青年遠征軍陸軍第二零一師師歌》（胡然 曲）
* [`youth_expeditionary_marching_suite.tmd`](youth-army/youth_expeditionary_marching_suite.tmd) — 《青年遠征軍行進組曲》（管樂／軍樂隊行進組曲）
* **[`new_first_army/`](youth-army/new_first_army/) — 《新一軍軍歌》（孫熙澤 詞、應雪痕 曲）**
  * [`new_first_army.tmd`](youth-army/new_first_army/new_first_army.tmd)（原曲）、[`new_first_army_march.tmd`](youth-army/new_first_army/new_first_army_march.tmd)（管弦進行曲版）
* 參考史料：[`青年軍歌集.pdf`](youth-army/青年軍歌集.pdf)

---

## 3. 日治時期公學校唱歌 (`kogakko_shoka/`)

完整書影與曲目索引參見 [`kogakko_shoka/index.md`](kogakko_shoka/index.md)（國立臺灣歷史博物館典藏《公學校唱歌》第三學年用，館藏號 `2020.006.0855`）：

* **連篇組曲改編**：
  * [`kogakko_shoka_grade3_chamber_suite.tmd`](kogakko_shoka/grade_3/kogakko_shoka_grade3_chamber_suite.tmd) — 《臺灣公學校唱歌（第三學年）室內樂組曲》
  * [`kogakko_shoka_grade3_chamber_fugue_suite.tmd`](kogakko_shoka/grade_3/kogakko_shoka_grade3_chamber_fugue_suite.tmd) — 《臺灣公學校唱歌（第三學年）室內樂組曲 — 終曲五主題大賦格版》
* [`grade_3/0_book_info/`](kogakko_shoka/grade_3/0_book_info/) — 封面、扉頁、目錄（もくろく）、版權頁與舊藏者手寫筆記
* [`grade_3/1_awoba/`](kogakko_shoka/grade_3/1_awoba/) — 第一課〈あをば〉（[`awoba.tmd`](kogakko_shoka/grade_3/1_awoba/awoba.tmd)）
* [`grade_3/2_daisha/`](kogakko_shoka/grade_3/2_daisha/) — 第二課〈だいしゃ（台車）〉（[`daisha.tmd`](kogakko_shoka/grade_3/2_daisha/daisha.tmd)、[`daisha_piano.tmd`](kogakko_shoka/grade_3/2_daisha/daisha_piano.tmd)）
* [`grade_3/3_muranokajiya/`](kogakko_shoka/grade_3/3_muranokajiya/) — 第三課〈村のかぢや〉（[`muranokajiya.tmd`](kogakko_shoka/grade_3/3_muranokajiya/muranokajiya.tmd)、[`muranokajiya_anime.tmd`](kogakko_shoka/grade_3/3_muranokajiya/muranokajiya_anime.tmd) 動漫熱血改編版）
* [`grade_3/4_gyusha/`](kogakko_shoka/grade_3/4_gyusha/) — 第四課〈牛車〉（[`gyusha.tmd`](kogakko_shoka/grade_3/4_gyusha/gyusha.tmd)）
* [`grade_3/5_nagaioyasumi/`](kogakko_shoka/grade_3/5_nagaioyasumi/) — 第五課〈ながいお休〉（[`nagaioyasumi.tmd`](kogakko_shoka/grade_3/5_nagaioyasumi/nagaioyasumi.tmd)）
* [`grade_3/6_semi/`](kogakko_shoka/grade_3/6_semi/) — 第六課〈せみ（蟬）〉（[`semi.tmd`](kogakko_shoka/grade_3/6_semi/semi.tmd)）
* [`grade_3/7_suiren/`](kogakko_shoka/grade_3/7_suiren/) — 第七課〈すゐれん（睡蓮）〉（[`suiren.tmd`](kogakko_shoka/grade_3/7_suiren/suiren.tmd)）
* [`grade_3/8_omatsuribi/`](kogakko_shoka/grade_3/8_omatsuribi/) — 第八課〈おまつり日（祭典之日）〉（[`omatsuribi.tmd`](kogakko_shoka/grade_3/8_omatsuribi/omatsuribi.tmd)）
* [`grade_3/9_niji/`](kogakko_shoka/grade_3/9_niji/) — 第九課〈にじ（彩虹）〉（[`niji.tmd`](kogakko_shoka/grade_3/9_niji/niji.tmd)）
* [`grade_3/10_undokai/`](kogakko_shoka/grade_3/10_undokai/) — 第十課〈うんどうくわい（運動會）〉（[`undokai.tmd`](kogakko_shoka/grade_3/10_undokai/undokai.tmd)）
* [`grade_3/11_kisha/`](kogakko_shoka/grade_3/11_kisha/) — 第十一課〈きしゃ（火車）〉（[`kisha.tmd`](kogakko_shoka/grade_3/11_kisha/kisha.tmd)）
* [`grade_3/12_dainippon/`](kogakko_shoka/grade_3/12_dainippon/) — 第十二課〈大日本〉（[`dainippon.tmd`](kogakko_shoka/grade_3/12_dainippon/dainippon.tmd)）
* [`grade_3/13_ojiisan/`](kogakko_shoka/grade_3/13_ojiisan/) — 第十三課〈おぢいさん（老爺爺）〉（[`ojiisan.tmd`](kogakko_shoka/grade_3/13_ojiisan/ojiisan.tmd)）
* [`grade_3/14_sumiyaki/`](kogakko_shoka/grade_3/14_sumiyaki/) — 第十四課〈すみやき（燒炭）〉（[`sumiyaki.tmd`](kogakko_shoka/grade_3/14_sumiyaki/sumiyaki.tmd)）
* [`grade_3/15_shirasagi/`](kogakko_shoka/grade_3/15_shirasagi/) — 第十五課〈白さぎ（白鷺鷥）〉（[`shirasagi.tmd`](kogakko_shoka/grade_3/15_shirasagi/shirasagi.tmd)）

---

## 4. 練習與實驗 (`uebung/`)

* [`canon_gen.py`](uebung/canon_gen.py) — 卡農對位演算法生成器
* [`king_canon.tmd`](uebung/king_canon.tmd) — 《王道 D 大調卡農》
* [`prac_canon.tmd`](uebung/prac_canon.tmd) — 《zonble's Canon in A Minor》
* [`b.tmd`](uebung/b.tmd) — 《B 小調實驗曲 (Experiment in B Minor)》（跨四個八度音域與花腔實驗）
* [`zonble-weird-stuff.tmd`](uebung/zonble-weird-stuff.tmd) — 《zonble's weird stuff》

---

## 5. 語法測試 (`golden_case/`)

* [`golden_case.tmd`](golden_case/golden_case.tmd) — 《Golden Case Fantasy》（TMD 全語法展示與極限壓力測試總覽）
