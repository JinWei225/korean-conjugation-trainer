from syllable_handler import decompose, recompose


def conjugate_ida(stem, honorific_type, tense, case="consonant", contracted=False):
    csnt_idx, vowel_idx, _ = decompose(stem)
    if honorific_type == "haeche":
        if tense == "present":
            if case == "consonant":
                return stem + "야"
            elif case == "vowel":
                return "야"
        elif tense == "past":
            if case == "consonant":
                return stem + "었어"
            elif case == "vowel":
                return "였어"
        elif tense == "future":
            return recompose(csnt_idx, vowel_idx, 8) + (
                " 거야" if contracted else " 것이야"
            )
    elif honorific_type == "haeyoche":
        if tense == "present":
            if case == "consonant":
                return stem + "에요"
            elif case == "vowel":
                return "예요"
        elif tense == "past":
            if case == "consonant":
                return stem + "었어요"
            elif case == "vowel":
                return "였어요"
        elif tense == "future":
            return recompose(csnt_idx, vowel_idx, 8) + (
                " 거예요" if contracted else " 것이에요"
            )
    elif honorific_type == "habsyoche":
        if tense == "present":
            return recompose(csnt_idx, vowel_idx, 17) + "니다"
        elif tense == "past":
            if case == "consonant":
                return stem + "었습니다"
            elif case == "vowel":
                return "였습니다"
        elif tense == "future":
            return recompose(csnt_idx, vowel_idx, 8) + (
                " 겁니다" if contracted else " 것입니다"
            )
    else:
        raise ValueError


ida_form = {
    "이야": [
        {
            "stem": "이",
            "honorific_type": "haeche",
            "tense": "present",
            "case": "consonant",
            "contracted": None,
        }
    ],
    "야": [
        {
            "stem": "이",
            "honorific_type": "haeche",
            "tense": "present",
            "case": "vowel",
            "contracted": None,
        }
    ],
    "이었어": [
        {
            "stem": "이",
            "honorific_type": "haeche",
            "tense": "past",
            "case": "consonant",
            "contracted": None,
        }
    ],
    "였어": [
        {
            "stem": "이",
            "honorific_type": "haeche",
            "tense": "past",
            "case": "vowel",
            "contracted": None,
        }
    ],
    "일 것이야": [
        {
            "stem": "이",
            "honorific_type": "haeche",
            "tense": "future",
            "case": "consonant",
            "contracted": False,
        },
        {
            "stem": "이",
            "honorific_type": "haeche",
            "tense": "future",
            "case": "vowel",
            "contracted": False,
        },
    ],
    "일 거야": [
        {
            "stem": "이",
            "honorific_type": "haeche",
            "tense": "future",
            "case": "consonant",
            "contracted": True,
        },
        {
            "stem": "이",
            "honorific_type": "haeche",
            "tense": "future",
            "case": "vowel",
            "contracted": True,
        },
    ],
    "이에요": [
        {
            "stem": "이",
            "honorific_type": "haeyoche",
            "tense": "present",
            "case": "consonant",
            "contracted": None,
        }
    ],
    "예요": [
        {
            "stem": "이",
            "honorific_type": "haeyoche",
            "tense": "present",
            "case": "vowel",
            "contracted": None,
        }
    ],
    "이었어요": [
        {
            "stem": "이",
            "honorific_type": "haeyoche",
            "tense": "past",
            "case": "consonant",
            "contracted": None,
        }
    ],
    "였어요": [
        {
            "stem": "이",
            "honorific_type": "haeyoche",
            "tense": "past",
            "case": "vowel",
            "contracted": None,
        }
    ],
    "일 것이에요": [
        {
            "stem": "이",
            "honorific_type": "haeyoche",
            "tense": "future",
            "case": "consonant",
            "contracted": False,
        },
        {
            "stem": "이",
            "honorific_type": "haeyoche",
            "tense": "future",
            "case": "vowel",
            "contracted": False,
        },
    ],
    "일 거예요": [
        {
            "stem": "이",
            "honorific_type": "haeyoche",
            "tense": "future",
            "case": "consonant",
            "contracted": True,
        },
        {
            "stem": "이",
            "honorific_type": "haeyoche",
            "tense": "future",
            "case": "vowel",
            "contracted": True,
        },
    ],
    "입니다": [
        {
            "stem": "이",
            "honorific_type": "habsyoche",
            "tense": "present",
            "case": "consonant",
            "contracted": None,
        },
        {
            "stem": "이",
            "honorific_type": "habsyoche",
            "tense": "present",
            "case": "vowel",
            "contracted": None,
        },
    ],
    "이었습니다": [
        {
            "stem": "이",
            "honorific_type": "habsyoche",
            "tense": "past",
            "case": "consonant",
            "contracted": None,
        }
    ],
    "였습니다": [
        {
            "stem": "이",
            "honorific_type": "habsyoche",
            "tense": "past",
            "case": "vowel",
            "contracted": None,
        }
    ],
    "일 것입니다": [
        {
            "stem": "이",
            "honorific_type": "habsyoche",
            "tense": "future",
            "case": "consonant",
            "contracted": False,
        },
        {
            "stem": "이",
            "honorific_type": "habsyoche",
            "tense": "future",
            "case": "vowel",
            "contracted": False,
        },
    ],
    "일 겁니다": [
        {
            "stem": "이",
            "honorific_type": "habsyoche",
            "tense": "future",
            "case": "consonant",
            "contracted": True,
        },
        {
            "stem": "이",
            "honorific_type": "habsyoche",
            "tense": "future",
            "case": "vowel",
            "contracted": True,
        },
    ],
}
combinations = [
    ("haeche", "present", None, "consonant"),
    ("haeche", "present", None, "vowel"),
    ("haeche", "past", None, "consonant"),
    ("haeche", "past", None, "vowel"),
    ("haeche", "future", False, "consonant"),
    ("haeche", "future", False, "vowel"),
    ("haeche", "future", True, "consonant"),
    ("haeche", "future", True, "vowel"),
    ("haeyoche", "present", None, "consonant"),
    ("haeyoche", "present", None, "vowel"),
    ("haeyoche", "past", None, "consonant"),
    ("haeyoche", "past", None, "vowel"),
    ("haeyoche", "future", False, "consonant"),
    ("haeyoche", "future", False, "vowel"),
    ("haeyoche", "future", True, "consonant"),
    ("haeyoche", "future", True, "vowel"),
    ("habsyoche", "present", None, "consonant"),
    ("habsyoche", "present", None, "vowel"),
    ("habsyoche", "past", None, "consonant"),
    ("habsyoche", "past", None, "vowel"),
    ("habsyoche", "future", False, "consonant"),
    ("habsyoche", "future", False, "vowel"),
    ("habsyoche", "future", True, "consonant"),
    ("habsyoche", "future", True, "vowel"),
]
if __name__ == "__main__":
    conjugation_ida_dict = {}
    stem = "이"
    honorifics = ["haeche", "haeyoche", "habsyoche"]
    tenses = ["present", "past", "future"]
    cases = ["consonant", "vowel"]
    conjugation_ida_dict[stem] = []
    try:
        for honorific in honorifics:
            for tense in tenses:
                if tense == "future":
                    for case in cases:
                        conjugation_ida_dict[stem].append(
                            {
                                "conjugation": conjugate_ida(
                                    stem, honorific, tense, case
                                ),
                                "honorific_type": honorific,
                                "tense": tense,
                                "case": case,
                                "contracted": False,
                            }
                        )
                        conjugation_ida_dict[stem].append(
                            {
                                "conjugation": conjugate_ida(
                                    stem, honorific, tense, case, True
                                ),
                                "honorific_type": honorific,
                                "tense": tense,
                                "case": case,
                                "contracted": True,
                            }
                        )
                else:
                    for case in cases:
                        conjugation_ida_dict[stem].append(
                            {
                                "conjugation": conjugate_ida(
                                    stem, honorific, tense, case
                                ),
                                "honorific_type": honorific,
                                "tense": tense,
                                "case": case,
                                "contracted": None,
                            }
                        )
    except ValueError:
        print("Error: There is a non-Hangul character! Please input again!")
    print(conjugation_ida_dict)
