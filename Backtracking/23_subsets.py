from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    res = []

    def backtrack(start, path):
        res.append(path[:])  # store a shallow copy (changes later must not affect)

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()  # remove the last - find more options.

    backtrack(0, [])
    return res


print(subsets([1, 2, 3]))