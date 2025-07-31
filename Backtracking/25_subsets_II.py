from typing import List


def subsets_II(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []

    def backtrack(start, path):
        last_seen = -100
        res.append(path[:])
        for i in range(start, len(nums)):
            if nums[i] == last_seen:
                continue

            path.append(nums[i])
            backtrack(i + 1, path)
            last_seen = path.pop()  # remove the last - find more options.

    backtrack(0, [])
    return res


print(subsets_II([1, 2, 2, 1]))
