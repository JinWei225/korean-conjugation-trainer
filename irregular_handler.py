from syllable_handler import decompose, replace_last_syllable


irregulars = {
    "ㅅ": ["짓", "낫", "씻"],
    "ㄷ": ["걷", "듣"],
    "ㅂ(우)": ["쉽", "어렵", "귀엽", "춥", "아름답", "새롭"],
    "ㅂ(오)": ["돕", "곱"],
    "ㅡ": ["잠그", "바쁘", "예쁘", "슬프", "크"],
    "르": ["다르", "빠르", "부르"],
    "ㄹ": ["길", "멀", "만들"],
}


def detect_irregulars(stem):
    if stem[-1] == "르":
        return "르"
    else:
        _, last_vowel_idx, last_final_idx = decompose(stem[-1])
        if last_final_idx == 7:  # ㄷ
            if stem in irregulars.get("ㄷ", []):
                return "ㄷ"
        elif last_final_idx == 8:  # ㄹ
            if stem in irregulars.get("ㄹ", []):
                return "ㄹ"
        elif last_final_idx == 17:  # ㅂ
            if stem in irregulars.get("ㅂ(우)", []):
                return "ㅂ(우)"
            if stem in irregulars.get("ㅂ(오)", []):
                return "ㅂ(오)"
        elif last_final_idx == 19:  # ㅅ
            if stem in irregulars.get("ㅅ", []):
                return "ㅅ"
        elif last_vowel_idx == 18:  # ㅡ
            if stem in irregulars.get("ㅡ", []):
                return "ㅡ"
        else:
            return None


# ㄷ irregular stem transformation
def transform_d_irregular(stem):
    last_csnt_idx, last_vowel_idx, _ = decompose(stem[-1])
    return replace_last_syllable(stem, last_csnt_idx, last_vowel_idx, 8)


# ㅅ irregular stem transformation
def transform_s_irregular(stem):
    last_csnt_idx, last_vowel_idx, _ = decompose(stem[-1])
    return replace_last_syllable(stem, last_csnt_idx, last_vowel_idx, 0)


if __name__ == "__main__":
    test_words = ["춥", "잡", "듣", "걸", "다르", "바쁘"]
    for word in test_words:
        print(f"Stem: {word}")
        print(f"Irregulars detected: {detect_irregulars(word)}")
