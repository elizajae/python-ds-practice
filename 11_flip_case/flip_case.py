def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    flipped = ""

    # Loop through each character in the phrase
    for char in phrase:
        # Check if the current character (case-insensitive) matches to_swap
        if char.lower() == to_swap.lower():
            # If it's a lowercase char, convert it to uppercase. 
            # If it's an uppercase char, convert it to lowercase.
            flipped += char.swapcase()
        else:
            # If it doesn't match the character to swap, keep it as it is
            flipped += char

    return flipped