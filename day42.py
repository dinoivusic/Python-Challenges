def pig_it(text):
    text = [x for x in text.split(" ")]
    mark = []
    print(text)
    for char in text:
        if char in '?!':
            text.remove(char)
            mark.append(char)
    print(mark)
    new = ["".join(word[1:]+word[0]+'ay') for word in text ]
    new.extend(mark)
    return " ".join(new)
