# counting duplicates
def duplicate_count(text):
    dic = {}
    count = 0
    for char in text.lower():
        if char not in dic:
            dic[char] = 1
        else:
            dic[char] += 1
    for key, value in dic.items():
        if value > 1:
            count += 1
    return count

