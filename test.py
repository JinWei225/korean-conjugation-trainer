from ida_handler import ida_form

irregulars = {
    "ㅅ": ["짓", "낫", "씻"],
    "ㄷ": ["걷", "듣"],
    "ㅂ(우)": ["쉽", "어렵", "귀엽", "춥", "아름답", "새롭"],
    "ㅂ(오)": ["돕", "곱"],
    "ㅡ": ["잠그", "바쁘", "예쁘", "슬프", "크"],
    "르": ["다르", "빠르", "부르"],
    "ㄹ": ["길", "멀", "만들"],
}
test_dict = {
    "춥": [
        {
            "conjugation": "추워",
            "honorific_type": "haeche",
            "tense": "present",
            "contracted": None,
            "irregular_type": "ㅂ(우)",
        }
    ],
    "피": [
        {
            "conjugation": "펴요",
            "honorific_type": "haeyoche",
            "tense": "present",
            "contracted": None,
            "irregular_type": None,
        }
    ],
    "펴": [
        {
            "conjugation": "펴요",
            "honorific_type": "haeyoche",
            "tense": "present",
            "contracted": None,
            "irregular_type": None,
        }
    ],
    "듣": [
        {
            "conjugation": "들어",
            "honorific_type": "haeche",
            "tense": "present",
            "contracted": None,
            "irregular_type": "ㄷ",
        }
    ],
    "들어": [
        {
            "stem": "듣",
            "honorific_type": "haeche",
            "tense": "present",
            "contracted": None,
            "irregular_type": "ㄷ",
        },
        {
            "stem": "들",
            "honorific_type": "haeche",
            "tense": "present",
            "contracted": None,
            "irregular_type": None,
        },
    ],
}
result = {
    "길어": [
        {
            "stem": "길",
            "honorific_type": "haeche",
            "tense": "present",
            "contracted": None,
            "irregular_type": "ㄹ",
        }
    ],
    "길었어": [
        {
            "stem": "길",
            "honorific_type": "haeche",
            "tense": "past",
            "contracted": None,
            "irregular_type": "ㄹ",
        }
    ],
    "길 것이야": [
        {
            "stem": "길",
            "honorific_type": "haeche",
            "tense": "future",
            "contracted": False,
            "irregular_type": "ㄹ",
        }
    ],
    "길 거야": [
        {
            "stem": "길",
            "honorific_type": "haeche",
            "tense": "future",
            "contracted": True,
            "irregular_type": "ㄹ",
        }
    ],
    "길어요": [
        {
            "stem": "길",
            "honorific_type": "haeyoche",
            "tense": "present",
            "contracted": None,
            "irregular_type": "ㄹ",
        }
    ],
    "길었어요": [
        {
            "stem": "길",
            "honorific_type": "haeyoche",
            "tense": "past",
            "contracted": None,
            "irregular_type": "ㄹ",
        }
    ],
    "길 것이에요": [
        {
            "stem": "길",
            "honorific_type": "haeyoche",
            "tense": "future",
            "contracted": False,
            "irregular_type": "ㄹ",
        }
    ],
    "길 거예요": [
        {
            "stem": "길",
            "honorific_type": "haeyoche",
            "tense": "future",
            "contracted": True,
            "irregular_type": "ㄹ",
        }
    ],
    "깁니다": [
        {
            "stem": "길",
            "honorific_type": "habsyoche",
            "tense": "present",
            "contracted": None,
            "irregular_type": "ㄹ",
        }
    ],
    "길었습니다": [
        {
            "stem": "길",
            "honorific_type": "habsyoche",
            "tense": "past",
            "contracted": None,
            "irregular_type": "ㄹ",
        }
    ],
    "길 것입니다": [
        {
            "stem": "길",
            "honorific_type": "habsyoche",
            "tense": "future",
            "contracted": False,
            "irregular_type": "ㄹ",
        }
    ],
    "길 겁니다": [
        {
            "stem": "길",
            "honorific_type": "habsyoche",
            "tense": "future",
            "contracted": True,
            "irregular_type": "ㄹ",
        }
    ],
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
if __name__ == "__main__":
    results = []
    for _, (conjugation, entries) in enumerate(ida_form.items()):
        for entry in entries:
            print(entry)
