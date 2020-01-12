def solution(number):
    new = []
    for i in range(1, number):
        if i % 5 == 0 and i % 3 == 0:
            new.append(i)
        if i % 3 == 0 or i % 5 == 0 :
            new.append(i)
    return sum(new)


print(solution(10))

# other way of doing it


def solutions(n):
    return sum(x for x in range(1,n) if x % 5 == 0 or x % 3 == 0)


print(solutions(10))