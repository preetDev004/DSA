from typing import List


def find_disappeared_numbers(nums: List[int]) -> List[int]:
    n_set = set(nums)
    missing = []

    for i in range(1, len(nums) + 1):
        if i not in n_set:
            missing.append(i)

    return missing


def find_disappeared_numbers_v2(nums: List[int]) -> List[int]:
    return list(set(range(len + 1)) - set(nums))


print(find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1]))
print(find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1]))
