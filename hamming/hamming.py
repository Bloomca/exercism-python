def distance(strand_a, strand_b):
    """
    Calculate Hamming distance between two DNA strands.

    GAGCCTACTAACGGGAT
    CATCGTAATGACGGCCT
    ^ ^ ^  ^ ^    ^^

    Distance is 7.

    >>> distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT")
    7

    >>> distance("GAGC", "CAT")
    ValueError: Length of both strands should be equal
    """
    if len(strand_a) != len(strand_b):
        raise ValueError("Length of both strands should be equal")
    
    return sum([
        1 if x != y else 0
        for (x, y) in zip(strand_a, strand_b)])
    
