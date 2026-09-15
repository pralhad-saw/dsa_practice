


def are_anagrams(first: str, second: str) -> bool:
    """
    Checks whether two strings contain the same characters
    with the same frequencies.
    Spaces, punctuation, and case are ignored.
    """
    first_clean = sorted(
        character.lower()
        for character in first
        if character.isalnum()
    )

    second_clean = sorted(
        character.lower()
        for character in second
        if character.isalnum()
    )

    return first_clean == second_clean


# Anagram
print(are_anagrams("listen", "silent"))       # True
print(are_anagrams("Dormitory", "Dirty room"))  # True
print(are_anagrams("hello", "world"))          # False
