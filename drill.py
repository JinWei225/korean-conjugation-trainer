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
    total_correct = 0
    total_words_completed = 0
    while len(conjugation_form) > 0:
        stem_bool = False
        honorific_bool = False
        tense_bool = False
        case_bool = False
        contracted_case_bool = False
        irregular_bool = False
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
        # print(f"Metadata: {form_data_chosen}")
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
        if stem_input == "이":
            case_input = input("Case (Vowel/Consonant/Both): ")
            while case_input.lower() not in ["vowel", "consonant", "both"]:
                print("Please choose from Vowel/Consonant/Both. Try again!\n")
                case_input = input("Case (Vowel/Consonant/Both): ")
        contracted_input = input("Contracted (Yes/No/None): ")
        while contracted_input.lower() not in ["yes", "no", "none"]:
            print("Please choose from Yes/No/None. Try again!\n")
            contracted_input = input("Contracted (Yes/No/None): ")
        if contracted_input.lower() == "yes":
            contracted_bool = True
        elif contracted_input.lower() == "no":
            contracted_bool = False
        else:
            contracted_bool = None
        if stem_input != "이":
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
            if irregular_input == "None" or irregular_input == "none":
                irregular_input = None
        print("\nResult:")
        if stem_input == form_data_chosen.get("stem"):
            print("✅ The stem is correct!")
            stem_bool = True
        else:
            print(
                f"❌ The stem is incorrect! The correct answer is {form_data_chosen.get("stem")}"
            )
        if honorific_input.lower() == form_data_chosen.get("honorific_type"):
            print("✅ The honorific type is correct!")
            honorific_bool = True
        else:
            print(
                f"❌ The honorific type is incorrect! The correct answer is {form_data_chosen.get("honorific_type")} type."
            )
        if tense_input.lower() == form_data_chosen.get("tense"):
            print("✅ The tense is correct!")
            tense_bool = True
        else:
            print(
                f"❌ The tense is incorrect! The correct answer is {form_data_chosen.get("tense")} tense."
            )
        if contracted_bool == form_data_chosen.get("contracted"):
            contracted_case_bool = True
            if form_data_chosen.get("contracted") == True:
                print("✅ This is a contracted form. ")
            elif form_data_chosen.get("contracted") == False:
                print("✅ This is not a contracted form. ")
            else:
                print(
                    "✅ There is no contracted or non-contracted form for this word. "
                )
        elif contracted_bool is not None and form_data_chosen.get("contracted") is None:
            print("❌ There is no contracted or uncontracted form for this word!")
        elif contracted_bool is None and form_data_chosen.get("contracted") is not None:
            print(
                "❌ This is a contracted form. "
                if form_data_chosen.get("contracted")
                else "❌ This is a uncontracted form. "
            )
        else:
            if form_data_chosen.get("contracted"):
                print("❌ This is a contracted form. ")
            else:
                print("❌ This is an uncontracted form. ")
        if stem_input == "이" and form_data_chosen.get("stem") == "이":
            if case_input == form_data_chosen.get("case"):
                print("✅ The case is correct!")
                case_bool = True
            else:
                print(
                    f"❌ The case is incorrect! The correct answer is {form_data_chosen.get("case")} case."
                )
        elif stem_input != "이" and form_data_chosen.get("stem") != "이":
            if irregular_input == form_data_chosen.get("irregular_type"):
                print("✅ The irregular type is correct!")
                irregular_bool = True
            else:
                print(
                    f"❌ The irregular type is incorrect! The correct answer is {form_data_chosen.get("irregular_type")}."
                )
        elif stem_input == "이" and form_data_chosen.get("stem") != "이":
            print(
                f"❌ The correct irregular type is {form_data_chosen.get("irregular_type")}."
            )
        elif stem_input != "이" and form_data_chosen.get("stem") == "이":
            print(f"❌ The correct case is {form_data_chosen.get("case")} case.")
        total_words_completed += 1
        if (
            stem_bool
            and honorific_bool
            and tense_bool
            and case_bool
            and contracted_case_bool
        ) or (
            stem_bool
            and honorific_bool
            and tense_bool
            and irregular_bool
            and contracted_case_bool
        ):
            total_correct += 1
        choice = input("Next? (Enter 'Y/y' to continue, 'N/n' to end this session): ")
        while choice.lower() not in ["y", "n"]:
            print("Please choose 'Y/y' or 'N/n'.")
            choice = input(
                "Next? (Enter 'Y/y' to continue, 'N/n' to end this program): "
            )
        if choice.lower() == "n":
            marks = float(total_correct) / total_words_completed * 100
            print(
                f"\nYou get {total_correct} out of {total_words_completed} forms correctly"
            )
            print(f"Your marks is {marks:.2f}")
            print("Program End")
            break
    if len(conjugation_form) == 0:
        print("\nYou have finished practising all the words. Congrats!")
        marks = float(total_correct) / total_words_completed * 100
        print(f"You get {total_correct} out of {total_words_completed} forms correctly")
        print(f"Your marks is {marks:.2f}")
