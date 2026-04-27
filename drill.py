import pickle
import random


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
    # Step 1
    with open("conjugation_form.pkl", "rb") as file:
        conjugation_form = pickle.load(file)
    # Step 2
    random_form = random.choice(list(conjugation_form))

    # Steo 3
    form_datas = conjugation_form.get(random_form)
    form_data_chosen = random.choice(form_datas)
    conjugation_form[random_form].remove(form_data_chosen)

    # Step 4
    if conjugation_form.get(random_form) == []:
        conjugation_form.pop(random_form)

    # Step 5
    print(f"Conjugated form: {random_form}\n")
    print(f"Metadata: {form_data_chosen}")
    stem_input = input("Stem: ")
    while not is_hangul(stem_input):
        print("Please enter hangul character. Try again!\n")
        stem_input = input("Stem: ")
    honorific_input = input("Honorific Type (Haeche/Haeyoche/Habsyoche): ")
    while honorific_input.lower() not in ["haeche", "haeyoche", "habsyoche"]:
        print("Please choose from Haeche/Haeyoche/Habsyoche. Try again!\n")
        honorific_input = input("Honorific Type (Haeche/Haeyoche/Habsyoche): ")
    tense_input = input("Tense (Present/Past/Future): ")
    while tense_input.lower() not in ["present", "past", "future"]:
        print("Please choose from Present/Past/Future. Try again!\n")
        tense_input = input("Tense (Present/Past/Future): ")
    contracted_input = input("Contracted (Yes/No): ")
    while contracted_input.lower() not in ["yes", "no"]:
        print("Please choose from Yes/No. Try again!\n")
        contracted_input = input("Contracted (Yes/No): ")
    contracted_bool = True if contracted_input == "yes" else False
    irregular_input = input(
        "Irregular Type [ㅅ, ㄷ, ㅂ(우), ㅂ(오), ㅡ, 르, ㄹ, None]: "
    )
    while irregular_input not in [
        "ㅅ",
        "ㄷ",
        "ㅂ(우)",
        "ㅂ(오)",
        "ㅡ",
        "르",
        "ㄹ",
        "None",
    ]:
        print(
            "Please choose from [ㅅ, ㄷ, ㅂ(우), ㅂ(오), ㅡ, 르, ㄹ, None]. Try again!\n"
        )
        irregular_input = input(
            "Irregular Type [ㅅ, ㄷ, ㅂ(우), ㅂ(오), ㅡ, 르, ㄹ, None]: "
        )
    print("\nResult:")
    print(
        "✅ The stem is correct!"
        if stem_input == form_data_chosen.get("stem")
        else f"❌ The stem is incorrect! The correct answer is {form_data_chosen.get("stem")}"
    )
    print(
        "✅ The honorific type is correct!"
        if honorific_input == form_data_chosen.get("honorific_type")
        else f"❌ The honorific type is incorrect! The correct answer is {form_data_chosen.get("honorific_type")} type."
    )
    print(
        "✅ The tense is correct!"
        if tense_input == form_data_chosen.get("tense")
        else f"❌ The tense is incorrect! The correct answer is {form_data_chosen.get("tense")} tense."
    )
    print(
        "✅ You are correct!"
        if contracted_bool == form_data_chosen.get("contracted")
        else " ❌You are wrong!"
    )
    print(
        (
            "This is a contracted form. "
            if form_data_chosen.get("contracted")
            else "This is not a contracted form. "
        )
    )
    print(
        "✅ The irregular type is correct!"
        if irregular_input == form_data_chosen.get("irregular_type")
        else f"❌ The irregular type is incorrect! The correct answer is {form_data_chosen.get("irregular_type")}."
    )
