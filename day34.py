def valid_parentheses(strng):
    BRACKET = {'(': ')', '{': '}', '[': ']'}
    bracket = []
    for a in strng:
        if a in BRACKET:
            bracket.append(BRACKET[a])
            continue
        try:
            if a == bracket.pop():
                continue
        except IndexError:
            pass
        return False
    return not bracket
