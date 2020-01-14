def tribonacci(n):
    a = 1
    b = 1
    c = 1
    if n == 0:
        return 0
    elif n == 1:
        return a
    elif n == 2:
        return b
    else:
        for i in range(3, n):
           d = a + b + c
           a = b
           b = c
           c = d
    return c