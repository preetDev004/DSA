import heapq
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int: # O(n log k)
        heap = nums[:k]
        heapq.heapify(heap) # O(k)

        for num in nums[k:]:
            print(heap)
            if heap[0] < num:
                heapq.heappushpop(heap, num) # O((n-k) * 2 log n)
        
        return heap[0]
    
sol = Solution()
arr = [1,3,5,7,32,13,2]
print(sol.findKthLargest(arr, 4))