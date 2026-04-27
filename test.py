from ida_handler import ida_form
import random

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


def is_hangul(word):
    for char in word:
        code = ord(char)
        if not (
            (code >= 0xAC00 and code <= 0xD7AF)
            or (code >= 0x1100 and code <= 0x11FF)
            or (code >= 0x3130 and code <= 0x318F)
            or (code >= 0xA960 and code <= 0xA97F)
            or (code >= 0xD7B0 and code <= 0xD7FF)
        ):
            return False
    return True


if __name__ == "__main__":
    user_input = input("Input: ")
    print(is_hangul(user_input))
