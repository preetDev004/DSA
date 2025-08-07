from typing import List

def sort_stack(stack: List[int]) -> List[int]:
    if len(stack) == 0:
        return stack

    sorted_stack = []
    while stack:
        num = stack.pop()
        while sorted_stack and sorted_stack[-1] > num:
            num_in_sorted = sorted_stack.pop()
            stack.append(num_in_sorted)
        sorted_stack.append(num)
    return sorted_stack


print(sort_stack([34,3,31,98,2,23]))