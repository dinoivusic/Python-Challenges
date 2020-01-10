# challenge 4 - square digits in an integer
def square_digits(num):
    x = list(str(num))
    sq = [int(y)**2 for y in x]
    s = int("".join(map(str, sq)))
    return s

# challenge 5 - Isogram

def is_isogram(string):
    if len(string) == 0:
        return True
    x = string.upper()
    for i in x:
        if x.count(i) > 1:
            return False
    return True
