#!/usr/bin/python3

""" Prime Game """

def isWinner(x, nums):
    """ Function that returns the winner of the game 
        Args:
            x: number of rounds
            nums: list of nums
        Returns:
            name of the player that won the most rounds
    """
    if x < 1 or not nums:
        return None

    max_n = max(nums)
    prime_count = sieve_prime_count(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


def sieve_prime_count(n):
    """ Returns the list of prime numbers up to n
        using the Sieve of Eratosthenes
    """
    if n < 2:
        return [0] * (n + 1)

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    prime_count = [0] * (n + 1)
    total_primes = 0
    for i in range(1, n + 1):
        if is_prime[i]:
            total_primes += 1
        prime_count[i] = total_primes

    return prime_count
