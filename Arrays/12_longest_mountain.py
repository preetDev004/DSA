from typing import List


def longest_mountain(arr: List[int]) -> int:
    res = 0
    n = len(arr)
    i = 1
    while i < n - 1:
        # Check if arr[i] is a peak
        if arr[i - 1] < arr[i] > arr[i + 1]:
            l = i - 1
            r = i + 1
            # Move left pointer to the start of the mountain
            while l > 0 and arr[l - 1] < arr[l]:
                l -= 1
            # Move right pointer to the end of the mountain
            while r < n - 1 and arr[r] > arr[r + 1]:
                r += 1
            res = max(res, r - l + 1)
            i = r  # Skip to the end of this mountain

        i += 1
    return res


print(longest_mountain([2, 1, 4, 7, 3, 2, 5]))