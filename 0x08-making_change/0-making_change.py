#!/usr/bin/python3

""" Determines the fewest number of coins needed to meet a given amount """


def makeChange(coins, total):
    """ Determines the fewest number of coins needed to meet a given amount """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    needed_coins = 0
    for coin in coins:
        if total / coin > 0:
            needed_coins = needed_coins + (total // coin)
            total = total % coin
        if not total:
            break

    if total != 0 or needed_coins == 0:
        return -1
    return needed_coins
