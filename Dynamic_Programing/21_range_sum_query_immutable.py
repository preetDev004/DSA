from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.dp = [0] * (len(nums))
        self.dp[0] = nums[0]

        for i in range(1, len(nums)):
            self.dp[i] = nums[i] + self.dp[i-1]

        print(self.dp)


    def sumRange(self, left: int, right: int) -> int:
        return self.dp[right] if left == 0 else self.dp[right] - self.dp[left-1]
    

nums = [1, 2, 3, 4, 5]
numArray = NumArray(nums)
print(numArray.sumRange(0, 2))
print(numArray.sumRange(1, 3))
print(numArray.sumRange(2, 4))