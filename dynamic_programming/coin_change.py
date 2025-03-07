import math


def solution(coins, amount):
    # bottom up
    dp = [0] * amount
    dp[0] = 0
    for index in range(1, amount):
        dp[index] =
        result = - math.inf
        for i in coins:
            result = max(result, )

    pass


if __name__ == '__main__':
    print(solution(coins=[1, 2, 5], amount=11))
