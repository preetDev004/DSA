from typing import List

def max_profit(prices: List[int]) -> int:
    profit = 0
    buy = 0
    sell = 1

    while sell < len(prices):
        if prices[sell] > prices[buy]:
            profit = max(profit, prices[sell] - prices[buy])
        else:
            buy = sell
        sell += 1

    return profit

def max_profit_2(prices: List[int]) -> int:
    profit = 0
    min_price = prices[0]

    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit

print(max_profit([7,1,5,3,6,4]))
print(max_profit_2([7,1,5,3,6,4]))