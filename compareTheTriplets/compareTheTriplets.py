def compareTheTriplets(a1, a2, a3, b1, b2, b3):
    arr_a = [a1, a2, a3]
    arr_b = [b1, b2, b3]
    max_a = max_b = 0
    for i in range(len(arr_a)):
        if arr_a[i] > arr_b[i]:
            max_a += 1
        elif arr_a[i] < arr_b[i]:
            max_b += 1
    return [max_a, max_b]
