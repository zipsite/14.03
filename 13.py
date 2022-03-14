def count_positives_sum_negatives(arr):
    pos = 0
    neg = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            pos = pos + 1
        elif arr[i] < 0:
            neg = neg + arr[i]
    if len(arr) == 0:
        return []
    else:
        return [pos, neg]