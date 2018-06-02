minimal_ord = 97
maximal_ord = 122
english_letters = sorted({chr(x) for x in range(minimal_ord, maximal_ord + 1)})

def is_pangram(sentence):
    letters_set = set()
    for letter in sentence:
        lower_letter = letter.lower()

        if minimal_ord <= ord(lower_letter) <= maximal_ord:
            letters_set.add(lower_letter)
        else:
            continue

    return sorted(letters_set) == english_letters
