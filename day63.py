
def overlap(arr,num):
    count = 0
    for i in range(len(arr)):
        if arr[i][0] == num or arr[i][1] == num:
            count+=1
        if num > arr[i][0] and num < arr[i][1]:
            count+=1
    return count

