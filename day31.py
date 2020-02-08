from itertools import permutations

def perm(string):
    x = sorted(string)
    pool = permutations(x)
    perms = ["".join(x) for x in pool]
    return perms

