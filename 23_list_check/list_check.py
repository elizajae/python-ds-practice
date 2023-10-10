def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """

    all_lists = True

    for item in lst:
        if not isinstance(item, list):
            all_lists = False

    return all_lists
