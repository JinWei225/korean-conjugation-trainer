# Korean Form Recognition Trainer — Project Progress
*Paste this at the start of a new chat when continuing work on this project.*  
*Use together with learning_context_jin_wei.md*

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
irregular_handler.py     — irregular verb lists and detection
```

---

## Completed: syllable_handler.py

- `decompose(syllable)` — decomposes a single Hangul syllable into `(consonant_index, vowel_index, final_index)` using Unicode arithmetic. Raises `ValueError` on non-Hangul input.
- `recompose(consonant_index, vowel_index, final_index=0)` — rebuilds a proper precomposed Hangul syllable from indices using the reverse grid formula
- `decompose_word(word)` — decomposes a full word into a list of index tuples, raises `ValueError` on non-Hangul characters

---

## Completed: conjugation_handler.py

- `get_stem(dictionary_form)` — strips 다 from dictionary form, raises `ValueError` if input does not end in 다
- `replace_last_syllable(stem, consonant_index, vowel_index, final_index=0)` — helper that replaces the last syllable of a stem with a recomposed syllable. Used throughout to handle vowel contractions cleanly.

**해체 (base forms — all other speech levels build on these):**
- `conjugate_haeche_present(stem)` — handles all vowel harmony and contraction cases (ㅏ/ㅗ → 아, 하 → 해, ㅗ → 봐, ㅜ → 줘, ㅣ → 져, absorption, complex vowels)
- `conjugate_haeche_past(stem)` — adds ㅆ (final index 20) to contracted present stem + 어
- `conjugate_haeche_future(stem, contracted=False)` — 것이야 (full) or 거야 (contracted)

**해요체 (해체 + 요):**
- `conjugate_haeyoche_present(stem)` — 해체 present + 요
- `conjugate_haeyoche_past(stem)` — 해체 past + 요
- `conjugate_haeyoche_future(stem, contracted=False)` — 것이에요 (full) or 거예요 (contracted)

**합쇼체:**
- `conjugate_habsyoche_present(stem)` — 습니다 / ㅂ니다 (final index 17)
- `conjugate_habsyoche_past(stem)` — swaps 어 from 해체 past with 습니다
- `conjugate_habsyoche_future(stem, contracted=False)` — 것입니다 (full) or 겁니다 (contracted)

---

## Completed: irregular_handler.py

`irregulars` dictionary — hardcoded irregular verb stems organised by type:

| Key | Description | Examples |
|-----|-------------|---------|
| `"ㅂ(우)"` | ㅂ irregular → 워 contraction | 춥, 어렵, 귀엽, 아름답, 새롭 |
| `"ㅂ(오)"` | ㅂ irregular → 와 contraction | 돕, 곱 |
| `"ㄷ"` | ㄷ irregular | 걷, 듣 |
| `"ㄹ"` | ㄹ stems (drop ㄹ before ㄴ/ㅂ) | 길, 멀, 만들 |
| `"ㅅ"` | ㅅ irregular | 짓, 낫, 씻 |
| `"ㅡ"` | 으 irregular (drop ㅡ before vowel) | 바쁘, 예쁘, 슬프, 잠그, 크 |
| `"르"` | 르 irregular (ㄹ added to previous syllable) | 다르, 빠르, 부르 |

`detect_irregulars(stem)` — returns the matching key string or `None`:
- 르: direct string check on last character
- ㄷ, ㄹ, ㅂ, ㅅ: final consonant index + `in` lookup against dictionary list
- ㅡ: vowel index 18 + `in` lookup
- ㅂ checks ㅂ(우) first, then ㅂ(오)

---

## Pending

- Irregular transformation functions for each category
- Integration of irregular detection into conjugation pipeline
- Special verbs: 이다 and its unique conjugation logic
- Reverse lookup data structure (stem → list of `(conjugated_form, rule_label)` tuples)
- Drill interface (terminal first, then web UI over local WiFi)
- Anki deck import
