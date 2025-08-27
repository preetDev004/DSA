from collections import deque
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0
        flight_map = {i:[] for i in range(n)}
        for s, d, c in flights:
            flight_map[s].append((d, c))
        
        q = deque([(src, 0)])

        while q and k > -1:

            for i in range(len(q)):
                from_city, cost = q.popleft()

                for to_city, next_cost in flight_map[from_city]:
                    if cost + next_cost < prices[to_city]:
                        prices[to_city] = cost + next_cost
                        q.append((to_city, prices[to_city]))
                
            k -= 1
        
        return prices[dst] if prices[dst] != float('inf') else -1
 


        