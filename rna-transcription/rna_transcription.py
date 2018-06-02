def to_rna(dna_strand):
    """
    Provides RNA complement for DNA sequence.

    Rules are the following:
    * `G` -> `C`
    * `C` -> `G`
    * `T` -> `A`
    * `A` -> `U`
    """

    result = ""
    for symbol in dna_strand:
        result += convert_symbol(symbol)

    return result

def convert_symbol(symbol):
    if symbol == "G":
        return "C"
    elif symbol == "C":
        return "G"
    elif symbol == "T":
        return "A"
    elif symbol == "A":
        return "U"
    else:
        raise ValueError("invalid symbol in DNA: {0}".format(symbol))


