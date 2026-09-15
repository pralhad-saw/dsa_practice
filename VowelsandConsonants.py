def count_vowels_consonants(text: str) -> tuple[int, int]:
    """
    Counts vowels and consonants.
    Numbers, spaces, and punctuation are ignored.
    """
    vowels = set("aeiou")
    vowel_count = 0
    consonant_count = 0

    for character in text.lower():
        if character.isalpha():
            if character in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count


# Count vowels and consonants
vowels, consonants = count_vowels_consonants("Hello World!")
print(vowels, consonants)      # 3 7
