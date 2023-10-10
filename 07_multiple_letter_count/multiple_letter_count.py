def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    # 1. Initialize an empty dictionary
    letter_count = {}

    # 2. Loop through each character
    for char in phrase:
        # 3. Check & Count
        if char not in letter_count:
            letter_count[char] = 1  # Add the character with a count of 1
        else:
            letter_count[char] += 1  # Increment the count of the character

    return letter_count