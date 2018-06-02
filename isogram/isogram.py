def is_isogram(string):
    """
    Check whether given string is an isogram or not.

    Isogram is a word which contains only unique letters,
    ignoring whitespaces and hyphens.
    Also, upper/lower case differences are ignored.

    >>> is_isogram("first")
    True
    >>> is_isogram("FIRST word")
    False
    """

    checker = {}
    for char in string:
        # we ignore 
        if char == " " or char == "-":
            continue
        lowered_char = char.lower()
        if lowered_char in checker:
            return False
        else:
            checker[lowered_char] = True

    return True
