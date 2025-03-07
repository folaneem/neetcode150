# TOP DOWN

def fib(n):
    cache = {0: 0, 1: 1}

    def f(val):
        if val in cache:
            return cache[val]
        else:
            cache[val] = f(val - 1) + f(val - 2)
            return cache[val]

    return f(n)


# BOTTOM UP
def fib2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]
    return dp[-1]


if __name__ == '__main__':
    print(fib(10))
    print(fib2(10))
