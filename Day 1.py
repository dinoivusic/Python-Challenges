
# challenge 1 - Capitalizing all words in a given string
def toJadenCase(string):
    return " ".join(s.capitalize() for s in string.split())

