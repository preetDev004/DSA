
import heapq
from collections import Counter, deque

def leastInterval(tasks, n):
    """
    Optimal solution using max heap and queue.
    Time Complexity: O(n * log(26)) = O(n) since we have at most 26 tasks
    Space Complexity: O(26) = O(1)
    """
    if n == 0:
        return len(tasks)
    
    # Count frequency of each task
    task_counts = Counter(tasks)
    
    # Create max heap (negative counts for max heap in Python)
    max_heap = [-count for count in task_counts.values()]
    heapq.heapify(max_heap)
    
    # Queue to track tasks that are cooling down: (count, available_time)
    cooldown_queue = deque()
    
    time = 0
    
    while max_heap or cooldown_queue:
        time += 1
        
        # Process task from heap if available
        if max_heap:
            count = heapq.heappop(max_heap)
            count += 1  # Decrease count (since it's negative)
            
            # If task still has remaining count, add to cooldown queue
            if count < 0:
                cooldown_queue.append((count, time + n))
        
        # Check if any task in cooldown queue is ready
        if cooldown_queue and cooldown_queue[0][1] <= time:
            heapq.heappush(max_heap, cooldown_queue.popleft()[0])
    
    return time
