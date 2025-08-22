from typing import List


def spiral_matrix(matrix: List[List[int]]) -> List[int]:
    result = []

    while matrix:
        # Add first row
        result += matrix.pop(0)

        # Add last elems of all others
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())

        # Add the last row in reverse
        if matrix:
            result += matrix.pop()[::-1]

        # Now in reverse Add first elems
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))

        return result


print(spiral_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
