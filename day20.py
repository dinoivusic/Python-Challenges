def move_zeros(arr):
    new, zero = [], []
    n = len(arr)
    for i in range(n):
        if arr[i] == int(0) or arr[i] == 0.0:
            if type(arr[i]) == float or type(arr[i]) == int:
                zero.append(arr[i])
            else: new.append(arr[i])
        else:
            new.append(arr[i])
    return new+zero
