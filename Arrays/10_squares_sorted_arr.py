from collections import deque
from typing import List


def squares_sorted_arr(nums: List[int]) -> List[int]:
    if not nums:
        return []

    res = deque()
    l, r = 0, len(nums) - 1

    while l <= r:
        left, right = abs(nums[l]), abs(nums[r])

        if right > left:
            res.appendleft(right * right)
            r -= 1
        else:
            res.appendleft(left * left)
            l += 1

        return list(res)


print(squares_sorted_arr([-4, -1, 0, 3, 10]))