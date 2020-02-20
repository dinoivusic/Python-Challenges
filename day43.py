def narcissistic(value):
    values = list(str(value))
    sums = 0
    for i in values:
        sums += int(i)**len(values)
    if value == sums:
        return True
    return False

