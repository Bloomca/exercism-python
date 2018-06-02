import re

def word_count(phrase):

    # this is a very "lispy" solution. Don't use it, I guess
    # I also hope to rewrite it one day in more "pythonic" way

    # we need to have list so we have `count` function
    words = list(
        # trim quotes from words
        map(lambda word: word.strip("'"),
            filter(None,
                   # get words by allowing letters, digits and quotes
                   re.split("[^a-z0-9\']+?", phrase.lower()))))

    return {word: words.count(word) for word in words}
