def climbing_stairs(n: int) -> int:
    count = [0] * (n + 2)
    count[0], count[1], count[2] = 0, 1, 2

    for i in range(3, n + 1):
        count[i] = count[i - 1] + count[i - 2]

    return count[n]


print(climbing_stairs(5))