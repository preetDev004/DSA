from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    # Bottom-up DP approach - Dividing into sub-problems and solving them to reuse later.
    dp = [amount + 1] * (
        amount + 1
    )  # Storing max/impossible num of coins for each possible sub amount
    dp[0] = 0  # to reach amount 0 we don't need any coins

    for i in range(1, amount + 1):
        for c in coins:
            if i - c >= 0:
                dp[i] = min(dp[i], 1 + dp[i - c])

    return dp[amount] if dp[amount] != (amount + 1) else -1


print(coin_change([1, 2, 5], 11))