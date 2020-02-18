from itertools import permutations
def anagrams(word, words):
    comb = permutations(word)
    c = list(word)
    new = set(comb)
    news,another=[],[]
    for chars in new:
        news.append("".join(chars))
    for w in words:
        if w in news:
            another.append(w)
    return another

