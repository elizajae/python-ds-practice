def is_odd_string(word):
    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.

    For example, these sum to 1, which is odd:
    
        >>> is_odd_string('a')
        True

        >>> is_odd_string('A')
        True

    These sum to 4, which is not odd:
    
        >>> is_odd_string('aaaa')
        False

        >>> is_odd_string('AAaa')
        False

    Longer example:
    
        >>> is_odd_string('amazing')
        True
    """
    # START SOLUTION

    # We could do this with a loop, but it's easier to use a list comprehension
    # to get a list of character positions, then sum that list.

    # We'll use ord() to get the character position of each letter. We'll
    # need to convert the letter to lowercase first, since ord() gives us
    # different values for uppercase and lowercase letters.

    # We'll use a generator expression to convert each letter to its
    # character position, then pass that to sum() to get the total.

    # We'll use % to see if the total is odd or even.

    total = 0

    for char in word:
        if char.islower():
            total += ord(char) - ord('a') + 1
        else:
            total += ord(char) - ord('A') + 1

    return total % 2 == 1