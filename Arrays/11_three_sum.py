from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    if len(nums) < 3 or len(nums) > 3000:
        return []
    res = []
    nums.sort()
    for i, n in enumerate(nums):
        if n > 0:
            break

        if n == nums[i - 1] and i > 0:
            continue

        l, r = i + 1, len(nums) - 1

        while l < r:
            total = n + nums[l] + nums[r]
            if total == 0:
                res.append([n, nums[l], nums[r]])
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                r -= 1
                l += 1
            elif total > 0:
                r -= 1
            elif total < 0:
                l += 1

    return res


print(three_sum([-1, 0, 1, 2, -1, -4]))