class NonRepeatingCharacterFinder:

    def find_first_non_repeating_character(characters):

        for i in characters:
            if characters.count(i) == 1:
                return i






