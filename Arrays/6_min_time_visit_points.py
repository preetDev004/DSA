from typing import List


def min_time_visit_points(points: List[List[int]]) -> int:
    min_time = 0
    x1, y1 = points.pop()

    while points:
        x2, y2 = points.pop()
        min_time += max(abs(x1 - x2), abs(y1 - y2))
        x1, y1 = x2, y2

    return min_time


print(min_time_visit_points([[1, 1], [3, 4], [-1, 0]]))
