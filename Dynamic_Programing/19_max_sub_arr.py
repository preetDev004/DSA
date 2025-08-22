from typing import List

def max_sub_arr(nums: List[int]) -> int:
        total = 0
        max_total = nums[0]

        for n in nums:
            if total < 0:
                total = 0
            total += n
            max_total = max(max_total, total)
        
        return max_total

print(max_sub_arr([-2,1,-3,4,-1,2,1,-5,4]))