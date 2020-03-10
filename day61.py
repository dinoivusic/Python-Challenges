def removNb(n):
    if n < 1:
        return []
    new = [x for x in range(n+1)]
    news = []
    print(sum(new))
    for a in range(len(new)):
        for b in range(1, len(new)):
            if (new[a] * new[b]) == (sum(new) - (new[a]+new[b])):
               news.append((new[a],new[b]))

    return news