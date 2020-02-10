def dirReduc(arr):
    left = []
    directions = {'NORTH': 'SOUTH', 'SOUTH': 'NORTH', 'WEST': 'EAST', 'EAST': 'WEST'}
    for i in arr:
        if left and directions[i] == left[-1]:
            left.pop()
        else:
            left.append(i)
    return left
