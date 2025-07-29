from typing import List


def contains_duplicate_II(nums: List[int], k: int) -> bool:
    visited = set()
    for i, n in enumerate(nums):
        if n in visited:
            return True
        visited.add(n)
        if i >= k:
            visited.remove(nums[i - k])

    return False
