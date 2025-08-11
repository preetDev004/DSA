
from collections import deque
from typing import List

def reverse_k_using_stack(q: List[int], k:int) -> List[int]:
    stack = []
    for _ in range(k):
        stack.append(q.popleft())
    
    while stack:
        q.append(stack.pop())

    for _ in range(len(q)-k):
        q.append(q.popleft())

    return q
q = deque([10,20,30,40,50,60,70,80,90])

print(reverse_k_using_stack(q, 5))