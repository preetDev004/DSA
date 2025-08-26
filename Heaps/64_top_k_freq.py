from ast import List
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return [-1]
        # O(n log k)
        count = Counter(nums)
        heap = []
        for n, freq in count.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, n))
            elif freq > heap[0][0]:
                heapq.heappushpop(heap, (freq, n))
        return [n for _, n in heap]