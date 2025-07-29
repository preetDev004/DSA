from typing import List

def min_size_subarray_sum(nums: List[int], target: int) -> int:
        l = total = 0
        min_len = float('inf')
        
        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                min_len = min(min_len, r-l+1)
                total -= nums[l]
                l += 1
            
        return 0 if min_len == float('inf') else min_len