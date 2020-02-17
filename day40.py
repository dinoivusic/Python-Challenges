def order_weight(strng):
    weight = strng.split()

    def sums_weight(num):
        return sum([int(x) for x in str(num)])

    weight.sort()
    weight.sort(key=sums_weight)

    return " ".join(weight)