from syllable_handler import decompose, recompose, replace_last_syllable
from irregular_handler import detect_irregulars, transform_irregular


# Present Tense Informal Low Respect Conjugation
def conjugate_haeche_present(stem, irregular_type=None):
    if irregular_type:
        stem = transform_irregular(stem)
    last_csnt_idx, last_vowel_idx, last_final_idx = decompose(stem[-1])
    if last_final_idx > 0:
        if last_vowel_idx == 0 or last_vowel_idx == 8:
            return stem + "아"
        else:
            return stem + "어"
    else:
        if irregular_type == "ㅂ(우)":
            return replace_last_syllable(stem, last_csnt_idx, 14)
        elif irregular_type == "ㅂ(오)":
            return replace_last_syllable(stem, last_csnt_idx, 9)
        if last_vowel_idx == 0:
            if last_csnt_idx == 18:
                # 하다 -> 해요 special case (0 -> 1)
                return replace_last_syllable(stem, last_csnt_idx, 1)
            elif irregular_type == "ㅅ":
                return stem + "아"
            else:
                # Absorb 아 and add 요 only
                return stem
        elif last_vowel_idx == 8:
            if irregular_type == "ㅅ":
                return stem + "아"
            # Contract ㅗ and ㅏ into ㅘ (8 -> 9)
            return replace_last_syllable(stem, last_csnt_idx, 9)
        elif last_vowel_idx == 13:
            if irregular_type == "ㅅ":
                return stem + "어"
            # Contract ㅜ and ㅓ into ㅝ (13 -> 14)
            return replace_last_syllable(stem, last_csnt_idx, 14)
        elif last_vowel_idx == 20:
            if irregular_type == "ㅅ":
                return stem + "어"
            # Contract ㅣ and ㅓ into ㅕ (20 -> 6)
            return replace_last_syllable(stem, last_csnt_idx, 6)
        elif last_vowel_idx == 4 or last_vowel_idx == 6:
            if irregular_type == "ㅅ":
                return stem + "어"
            # Absorb 어 and add 요 only
            return stem
        else:
            # Complex vowels like ㅐ,ㅔ etc either add 어요 or just 요 is acceptable
            return stem


# Past Tense Informal Low Respect Conjugation
def conjugate_haeche_past(stem, irregular_type=None):
    present_form = conjugate_haeche_present(stem, irregular_type)  # 먹 -> 먹어
    last_csnt_idx, last_vowel_idx, _ = decompose(present_form[-1])
    return replace_last_syllable(present_form, last_csnt_idx, last_vowel_idx, 20) + "어"


# Future Tense Informal Low Respect Conjugation
def conjugate_haeche_future(stem, irregular_type=None, contracted=False):
    last_csnt_idx, last_vowel_idx, last_final_index = decompose(stem[-1])
    if last_final_index > 0 or irregular_type == "ㅅ":
        return stem + ("을 거야" if contracted else "을 것이야")
    else:
        return replace_last_syllable(stem, last_csnt_idx, last_vowel_idx, 8) + (
            " 거야" if contracted else " 것이야"
        )


# Present Tense Informal High Respect Conjugation
def conjugate_haeyoche_present(stem, irregular_type=None):
    haeche_form = conjugate_haeche_present(stem, irregular_type)
    return haeche_form + "요"


# Past Tense Informal High Respect Conjugation
def conjugate_haeyoche_past(stem, irregular_type=None):
    haeche_form = conjugate_haeche_past(stem, irregular_type)
    return haeche_form + "요"


# Future Tense Informal High Respect Conjugation
def conjugate_haeyoche_future(stem, irregular_type=None, contracted=False):
    haeche_form = conjugate_haeche_future(stem, irregular_type, contracted)
    return haeche_form[:-1] + ("예요" if contracted else "에요")


# Present Tense Formal High Respect Conjugation
def conjugate_habsyoche_present(stem, irregular_type=None):
    last_csnt_idx, last_vowel_idx, last_final_index = decompose(stem[-1])
    if irregular_type == "ㄹ":
        return replace_last_syllable(stem, last_csnt_idx, last_vowel_idx, 17) + "니다"
    if last_final_index > 0:
        return stem + "습니다"
    else:
        return replace_last_syllable(stem, last_csnt_idx, last_vowel_idx, 17) + "니다"


# Past Tense Formal High Respect Conjugation
def conjugate_habsyoche_past(stem, irregular_type=None):
    haeche_form = conjugate_haeche_past(stem, irregular_type)
    return haeche_form[:-1] + "습니다"


# Future Tense Formal High Respect Conjugation
def conjugate_habsyoche_future(stem, irregular_type=None, contracted=False):
    haeche_form = conjugate_haeche_future(stem, irregular_type, contracted)
    return haeche_form[:-2] + ("겁니다" if contracted else "입니다")


def get_stem(dictionary_form):
    if len(dictionary_form) > 1 and dictionary_form[-1] == "다":
        return dictionary_form[:-1]
    else:
        raise ValueError


if __name__ == "__main__":
    test_stem = [
        # "돕",
        # "춥",
        # "듣",
        # "짓",
        "바쁘",
        "다르",
    ]
    for stem in test_stem:
        try:
            print(f"Stem: {stem}")
            irregular_type = detect_irregulars(stem)
            print("--Haeche--")
            present_conjugated_word = conjugate_haeche_present(stem, irregular_type)
            past_conjugated_word = conjugate_haeche_past(stem, irregular_type)
            future_conjugated_word_full = conjugate_haeche_future(stem, irregular_type)
            future_conjugated_word_contracted = conjugate_haeche_future(
                stem, irregular_type, True
            )
            print(f"Conjugated Present Tense Form: {present_conjugated_word}")
            print(f"Conjugated Past Tense Form: {past_conjugated_word}")
            print(f"Conjugated Future Tense Form (Full): {future_conjugated_word_full}")
            print(
                f"Conjugated Future Tense Form: {future_conjugated_word_contracted}\n"
            )
            print("\n--Haeyoche--")
            present_conjugated_word = conjugate_haeyoche_present(stem, irregular_type)
            past_conjugated_word = conjugate_haeyoche_past(stem, irregular_type)
            future_conjugated_word_full = conjugate_haeyoche_future(
                stem, irregular_type
            )
            future_conjugated_word_contracted = conjugate_haeyoche_future(
                stem, irregular_type, True
            )
            print(f"Conjugated Present Tense Form: {present_conjugated_word}")
            print(f"Conjugated Past Tense Form: {past_conjugated_word}")
            print(f"Conjugated Future Tense Form (Full): {future_conjugated_word_full}")
            print(
                f"Conjugated Future Tense Form: {future_conjugated_word_contracted}\n"
            )
            print("\n--Habsyoche--")
            present_conjugated_word = conjugate_habsyoche_present(stem, irregular_type)
            past_conjugated_word = conjugate_habsyoche_past(stem, irregular_type)
            future_conjugated_word_full = conjugate_habsyoche_future(
                stem, irregular_type
            )
            future_conjugated_word_contracted = conjugate_habsyoche_future(
                stem, irregular_type, True
            )
            print(f"Conjugated Present Tense Form: {present_conjugated_word}")
            print(f"Conjugated Past Tense Form: {past_conjugated_word}")
            print(f"Conjugated Future Tense Form (Full): {future_conjugated_word_full}")
            print(
                f"Conjugated Future Tense Form: {future_conjugated_word_contracted}\n"
            )
        except ValueError:
            print("Error: There is a non-Hangul character! Please input again!")


# word_indices_list = decompose_word(word)
# for word_indices in word_indices_list:
#     consonant_idx, vowel_idx, final_idx = word_indices
#     original_syllable = recompose(consonant_idx, vowel_idx, final_idx)
#     print(
#         f"Consonant index: {consonant_idx}\nVowel index: {vowel_idx}\nFinal index: {final_idx}\nOriginal syllable: {original_syllable}\n"
#     )
