def verify(isbn):
    """
    Verify ISBN-10 number.
    (https://en.wikipedia.org/wiki/International_Standard_Book_Number)

    >>> verify('3-598-21508-8')
    True
    """
    filtered_isbn = remove_hyphens(isbn)
    length = len(filtered_isbn)

    if length < 10:
        return False

    result = 0
    for i in range(length):
        symbol = filtered_isbn[i]
        is_last = i == length - 1
        try:
            result += get_number(symbol, is_last=is_last) * (length - i)
        except ValueError:
            return False

    return result % 11 == 0

def get_number(symbol, is_last=False):
    """
    Convert symbol to int object.

    Allows to get "X" only if it is the last character,
    and returns 10 for it. Otherwise, raises ValueError.
    """
    if symbol == "X":
        if is_last:
            return 10
        else:
            raise ValueError("X is allowed only in the end")
    else:
        return int(symbol)

def remove_hyphens(isbn):
    """
    Remove hyphens from the given string.
    """
    result = ""
    for letter in isbn:
        if letter == "-":
            continue
        else:
            result += letter

    return result