from typing import List


def timeRequiredToBuy(tickets: List[int], k: int) -> int:
    seconds = 0
    while k != 0 or tickets[k] - 1 != 0:
        seconds += 1
        tickets[0] -= 1
        tickets.pop(0) if tickets[0] == 0 else tickets.append(tickets.pop(0))
        k = len(tickets) - 1 if k == 0 else k - 1

    return seconds + 1


def timeRequiredToBuy_v2(tickets: List[int], k: int) -> int:
    sec = 0
    for i in range(len(tickets)):
        sec += (
            min(tickets[i], tickets[k]) if i <= k else min(tickets[i], tickets[k] - 1)
        )

    return sec
