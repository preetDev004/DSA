from typing import List


def min_absolute_diff(arr: List[int]) -> int:
    n = len(arr)
    if n < 2:
        return [[]]
    arr.sort()
    res = []
    min_diff = float("inf")

    for i in range(n - 1):
        diff_at_i = abs(arr[i] - arr[i + 1])
        if min_diff > diff_at_i:
            min_diff = diff_at_i
            res.clear()
            res.append([arr[i], arr[i + 1]])
            
        elif diff_at_i == min_diff:
            res.append([arr[i], arr[i + 1]])

    return res


print(min_absolute_diff([4, 2, 1, 3]))
