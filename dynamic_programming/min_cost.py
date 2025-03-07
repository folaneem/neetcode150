def min_cost_climbing(n):
    size = len(n)
    dp = [0] * (size + 1)
    dp[0] = 0
    dp[1] = 0

    for index in range(2, size + 1):
        dp[index] = min(dp[index - 1] + n[index - 1], dp[index - 2] + n[index - 2])
    print(dp)
    return dp[-1]


print(min_cost_climbing(n=[10, 15, 5, 30, 4, 4, 10]))


def min_cost_climbing2(n):
    cache = {0: 0, 1: 0}

    def f(val):
        if val in cache:
            return cache.get(val)
        cache[val] = min(f(val - 1) + n[val - 1], f(val - 2) + n[val - 2])
        return cache[val]

    return f(val=len(n))


print(min_cost_climbing2(n=[10, 15, 5, 30, 4, 4, 10]))
