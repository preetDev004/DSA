from typing import List


def smaller_numbers_than_current(nums: List[int]) -> List[int]:
    sorted_nums = sorted(nums)
    nMap = {}

    for i, n in enumerate(sorted_nums):
        if n not in nMap:
            nMap[n] = i
    result = []
    for i, n in enumerate(nums):
        result.append(nMap[n])
    return result


print(smaller_numbers_than_current([8, 1, 2, 2, 3]))
