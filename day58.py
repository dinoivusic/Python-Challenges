def rev(string, sentence):
    x = string.split()
    new = []
    print(x)
    for word in x:
        if sentence == 'word':
            for y in x:
                i = y[::-1]
                new.append(i)
            return ' '.join(new)
        if sentence == 'sentence':
            yy = x[::-1]
            return ' '.join(yy)


print(rev(####, 'word'))
