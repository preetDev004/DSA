from typing import List 

def permute(nums: List[int]) -> List[List[int]]:
    res = []

    def backtrack(start, end):
        if start == end:
            res.append(nums[:])
            return

        for i in range(start, end):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start+1, end)
            nums[start], nums[i] = nums[i], nums[start]

    backtrack(0, len(nums))
    return res

print(permute([1,2,3]))