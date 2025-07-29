from typing import List


def single_number(nums: List[int]) -> int:
    xor = 0
    for i in range(len(nums)):
        xor = xor ^ nums[i]

    return xor


print(single_number([4, 1, 2, 1, 2]))