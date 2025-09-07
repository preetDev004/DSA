from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # solution 1 - time complexity: O(n), space complexity: O(1)
        # max_reach_index = 0
        # for i, n in enumerate(nums):
        #     if max_reach_index < i:
        #         return False
        #     elif max_reach_index >= len(nums):
        #         return True
        #     max_reach_index = max(max_reach_index,i+n)
        # return True

        # solution 2 - time complexity: O(n), space complexity: O(1)
        goal = len(nums) - 1

        for i in range(len(nums)-1, -1, -1):
            if i+nums[i] >= goal: # if current index + num reach to goal
                goal = i # reduce goal current index
        return True if goal == 0 else False
            
        