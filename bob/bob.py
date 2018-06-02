import re

def hey(original_phrase):
    """
    Response (in a very chill way) to anything.
    """
    phrase = original_phrase.strip()
    is_yelling = phrase.upper() == phrase and re.search("[A-Z]", phrase) is not None

    if not phrase or not phrase.strip():
        return "Fine. Be that way!"
    if phrase.endswith('?') and is_yelling and phrase:
        return "Calm down, I know what I'm doing!"
    elif is_yelling:
        return "Whoa, chill out!"
    elif phrase.endswith("?"):
        return "Sure."
        
    return "Whatever."
