# Decompose Hangul syllable into jamo
def decompose(syllable):
    if ord(syllable) < 0xAC00 or ord(syllable) > 0xD7A3:
        raise ValueError
    syllable_code = ord(syllable) - 0xAC00
    final_index = syllable_code % 28
    remaining = syllable_code // 28
    vowel_index = remaining % 21
    consonant_index = remaining // 21
    return consonant_index, vowel_index, final_index


# Recompose Hangul syllable from jamo
def recompose(consonant_index, vowel_index, final_index=0):
    return chr((consonant_index * 21 * 28) + (vowel_index * 28) + final_index + 0xAC00)


def decompose_word(word):
    return [(decompose(syllable)) for syllable in word]


def replace_last_syllable(stem, consonant_index, vowel_index, final_index=0):
    return (stem[:-1] if len(stem) > 1 else "") + recompose(
        consonant_index, vowel_index, final_index
    )


if __name__ == "__main__":
    syllable = "들"
    consonant_idx, vowel_idx, final_idx = decompose(syllable)
    original_syllable = recompose(consonant_idx, vowel_idx, final_idx)
    print(
        f"Syllable: {syllable}\nConsonant index: {consonant_idx}\nVowel index: {vowel_idx}\nFinal index: {final_idx}\nOriginal syllable: {original_syllable}"
    )
