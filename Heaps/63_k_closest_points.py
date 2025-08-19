from typing import List
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]: # O(n log k)
        heap = []
        for (x, y) in points:
            dist = -(x * x + y * y)
            if len(heap)==k:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
                
        return[[x,y] for (dist, x, y) in heap]

    def kClosest_v2(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda p: p[0] ** 2 + p[1] ** 2)[:k]