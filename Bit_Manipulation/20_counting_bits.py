from typing import List


def counting_bits(n: int) -> List[int]:
    dp = [0] * (n + 1)
    offset = 1

    for i in range(1, n + 1):
        if offset * 2 == i:
            offset = i  # every 2^x (2, 4, 8, 16, ...) our offset changes

        dp[i] = 1 + dp[i - offset]  # Recognised pattern

    return dp


print(counting_bits(8))

# 00000
# 00001
# 00010 # offset = 2
# 00011
# 00100 # offset = 4
# 00101
# 00110
# 00111  
# 01000 # offset = 8
