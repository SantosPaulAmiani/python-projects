def lam(arr):
    max1 = arr[0]
    min1 = arr[0]

    for x in arr:
        if x > max1:
            max1 = x
        elif x < min1:
            min1 = x

    return max1, min1

arr = [1, 3, 5, 5, 6, 78, 14]
print(lam(arr))
