from typing import List

def combinations(n: int, k: int) -> List[List[int]]:
    res = []

    def backtrack(start, path):
        if len(path) == k:
            res.append(path[:])
            return
        
        for i in range(start, n + 1):   # start from 1 to n
            path.append(i)
            backtrack(i + 1, path)
            path.pop()  # remove the last - find more options.

    backtrack(1, [])
    return res


print(combinations(4, 2))