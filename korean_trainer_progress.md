# Korean Form Recognition Trainer — Project Progress

_Paste this at the start of a new chat when continuing work on this project._  
_Use together with learning_context_jin_wei.md_

---

## Project Goal

Build a conjugation-aware Korean vocabulary trainer that drills recognition of verb forms beyond dictionary form. Motivated by difficulty recognising conjugated and honorific forms in natural speech and text.

---

## Architecture Decisions

- **Terminal prototype first**, then Flask/FastAPI web app accessible from phone over local WiFi (e.g. `192.168.x.x:8000`)
- **Reverse lookup approach:** pre-generate all conjugated forms from known stems, store in dictionary, drill via lookup rather than real-time parsing — avoids vowel contraction ambiguity problem
- **Vocab seeded from existing Anki deck**
- **Speech level terminology follows HTSK's three-tier system:** 해체 (informal low respect) / 해요체 (informal high respect) / 합쇼체 (formal high respect)

---

## File Structure

```
syllable_handler.py      — Hangul decomposition and recomposition
conjugation_handler.py   — stemming and conjugation logic
irregular_handler.py     — irregular verb lists, detection, and transformation
```

---

## Completed: syllable_handler.py

- `decompose(syllable) -> tuple` — decomposes a single Hangul syllable into `(consonant_index, vowel_index, final_index)` using Unicode arithmetic. Raises `ValueError` on non-Hangul input.
- `recompose(consonant_index, vowel_index, final_index=0) -> str` — rebuilds a proper precomposed Hangul syllable from indices using the reverse grid formula
- `decompose_word(word) -> list` — decomposes a full word into a list of index tuples, raises `ValueError` on non-Hangul characters

---

## Completed: conjugation_handler.py

- `get_stem(dictionary_form) -> str` — strips 다 from dictionary form, raises `ValueError` if input does not end in 다
- `replace_last_syllable(stem, consonant_index, vowel_index, final_index=0) -> str` — helper that replaces the last syllable of a stem with a recomposed syllable

**해체 (base forms — all other speech levels build on these):**

- `conjugate_haeche_present(stem, irregular_type=None) -> str` — handles all vowel harmony, contraction cases, and irregular-specific branches (ㅂ(우)/ㅂ(오) contraction, ㅅ no-contraction). Calls `transform_irregular` internally when `irregular_type` is provided.
- `conjugate_haeche_past(stem, irregular_type=None) -> str` — adds ㅆ (final index 20) to contracted present stem + 어
- `conjugate_haeche_future(stem, irregular_type=None, contracted=False) -> str` — 것이야 (full) or 거야 (contracted). ㅅ irregular uses 을 것이야 form.

**해요체 (해체 + 요):**

- `conjugate_haeyoche_present(stem, irregular_type=None) -> str`
- `conjugate_haeyoche_past(stem, irregular_type=None) -> str`
- `conjugate_haeyoche_future(stem, irregular_type=None, contracted=False) -> str`

**합쇼체:**

- `conjugate_habsyoche_present(stem, irregular_type=None) -> str` — ㄹ irregular handled directly (replace ㄹ final with ㅂ). Uses original stem (not transformed) since 습니다 is consonant-initial.
- `conjugate_habsyoche_past(stem, irregular_type=None) -> str`
- `conjugate_habsyoche_future(stem, irregular_type=None, contracted=False) -> str`

---

## Completed: irregular_handler.py

**`irregulars` dictionary:**

| Key        | Description                                  | Examples                     |
| ---------- | -------------------------------------------- | ---------------------------- |
| `"ㅂ(우)"` | ㅂ irregular → 워 contraction                | 춥, 어렵, 귀엽, 아름답, 새롭 |
| `"ㅂ(오)"` | ㅂ irregular → 와 contraction                | 돕, 곱                       |
| `"ㄷ"`     | ㄷ irregular                                 | 걷, 듣                       |
| `"ㄹ"`     | ㄹ stems (drop ㄹ before ㄴ/ㅂ)              | 길, 멀, 만들                 |
| `"ㅅ"`     | ㅅ irregular                                 | 짓, 낫, 씻                   |
| `"ㅡ"`     | 으 irregular (drop ㅡ, merge with 아/어)     | 바쁘, 예쁘, 슬프, 잠그, 크   |
| `"르"`     | 르 irregular (ㄹ added to previous syllable) | 다르, 빠르, 부르             |

**Functions:**

- `detect_irregulars(stem) -> str | None` — returns matching key or None
- `transform_irregular(stem) -> str` — routes to correct transformation function, returns original stem if no match
- `transform_d_irregular(stem) -> str` — replaces ㄷ final with ㄹ (index 8)
- `transform_s_irregular(stem) -> str` — removes ㅅ final (index 0)
- `transform_b_irregular(stem) -> str` — drops ㅂ, appends 우 (와/워 contraction handled in conjugate_haeche_present via irregular_type)
- `transform_eu_irregular(stem) -> str` — handles both ㅡ and 르. Uses second-to-last syllable vowel for 아/어 selection. Returns fully contracted form (e.g. 바빠, 달라).

**Key design decisions:**

- ㄹ irregular handled in `conjugate_habsyoche_present` directly, not via transform pipeline
- ㅅ irregular uses original stem for 합쇼체 present (consonant-initial ending), transformed stem for all others
- ㅂ(오) and ㅂ(우) both transform to stem + 우; distinction between 와/워 handled inside `conjugate_haeche_present` via `irregular_type` parameter
- All transformation functions have explicit `-> str` return type hints to avoid linter warnings

---

## Completed: ida_handler.py

**`conjugate_ida(stem, honorific_type, tense, case="consonant", contracted=False) -> str`:**

- `stem` is always `"이"`
- `case` is `"consonant"` or `"vowel"` — reflects whether the preceding noun ends in a consonant or vowel
- `contracted` applies to future tense only
- Raises `ValueError` for invalid `honorific_type`

**Conjugation table:**

| honorific_type | tense   | case      | contracted | result      |
| -------------- | ------- | --------- | ---------- | ----------- |
| 해체           | present | consonant | —          | 이야        |
| 해체           | present | vowel     | —          | 야          |
| 해체           | past    | consonant | —          | 이었어      |
| 해체           | past    | vowel     | —          | 였어        |
| 해체           | future  | either    | False      | 일 것이야   |
| 해체           | future  | either    | True       | 일 거야     |
| 해요체         | present | consonant | —          | 이에요      |
| 해요체         | present | vowel     | —          | 예요        |
| 해요체         | past    | consonant | —          | 이었어요    |
| 해요체         | past    | vowel     | —          | 였어요      |
| 해요체         | future  | either    | False      | 일 것이에요 |
| 해요체         | future  | either    | True       | 일 거예요   |
| 합쇼체         | present | either    | —          | 입니다      |
| 합쇼체         | past    | consonant | —          | 이었습니다  |
| 합쇼체         | past    | vowel     | —          | 였습니다    |
| 합쇼체         | future  | either    | False      | 일 것입니다 |
| 합쇼체         | future  | either    | True       | 일 겁니다   |

**`ida_forms` dictionary:**

- Key: `"이"`
- Value: list of dicts, each with keys `conjugation`, `honorific_type`, `tense`, `case`, `contracted`
- Stored separately from the main reverse lookup dictionary; drill interface will query both during lookup
- Future tense entries are duplicated for consonant/vowel cases (identical results — can be simplified later)

**Key design decisions:**

- 이다 lives in its own file (`ida_handler.py`) since it does not share the stem/conjugation pipeline of regular and irregular verbs
- Drill shows only the ending (e.g. `이에요`, `야`) — caller is responsible for attaching to noun if needed for display
- `case` field retained on future tense entries for structural consistency, though the conjugated form is identical regardless of case

---

## Next: Reverse Lookup & Drill Interface

**Reverse lookup approach:**

1. User inputs a word in dictionary form (e.g. `춥다`)
2. System calls `get_stem`, detects irregular type, then generates all conjugated forms using conjugation functions
3. Each form is stored in a lookup dictionary: `conjugated_form → list of (dictionary_form, rule_label)` tuples
4. `ida_forms` is queried separately during lookup and merged at drill time

**Drill interface (terminal prototype):**

- Display a conjugated form to the user
- User inputs the dictionary form and identifies the grammar rules applied (honorific type, tense, case if 이다)
- System checks answer against lookup dictionary
- Terminal first, then Flask/FastAPI web UI over local WiFi

**Pending:**

- Reverse lookup data structure and population logic
- Drill algorithm (word selection, answer checking, scoring)
- Terminal UI
- Anki deck import
- Flask/FastAPI web app
