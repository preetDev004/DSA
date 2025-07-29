from typing import List

def missing_number(nums: List[int]) -> int:
        return sum(range(len(nums)+1)) - sum(nums)
            # nums.sort()
            # for i, n in enumerate(nums):
            #     if i != n:
            #         return i
            # return len(nums)
        
print(missing_number([3,0,1]))