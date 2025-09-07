from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # solution 1 - time complexity: O(n), space complexity: O(n)
        # n = len(height)
        # sufix = [0] * n
        # sufix[n-1] = height[n-1]
        # r = n-2
        # while r >= 0:
        #     sufix[r] = max(sufix[r+1], height[r])
        #     r -= 1
        # water_stored = 0
        # max_l = 0
        # for i in range(n):
        #     max_l = max(max_l, height[i])
        #     if max_l and sufix[i]:
        #         water_stored += min(max_l, sufix[i]) - height[i]

        # return water_stored

        # solution 2 - time complexity: O(n), space complexity: O(1)
        max_l = max_r = water = 0
        l, r = 0, len(height) - 1

        while l < r: # both will end up to the largest block
            if height[l] <= height[r]:
                if max_l > height[l]:
                    water += max_l - height[l]
                else:
                    max_l = height[l]
                l += 1
            else:
                if max_r > height[r]:
                    water += max_r - height[r]
                else:
                    max_r = height[r]
                r -= 1
        return water
    
        
            
