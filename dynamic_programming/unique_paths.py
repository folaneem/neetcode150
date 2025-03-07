def unique_path(m, n):
    cache = {(0, 0): 1}

    def f(i, j):
        if (i, j) in cache:
            return cache.get((i, j))
        elif i < 0 or j < 0 or i == m or j == n:
            return 0
        else:
            cache[(i, j)] = f(i, j - 1) + f(i - 1, j)
            return cache[(i, j)]

    return f(m - 1, n - 1)


def bottom_up_unique_path(m, n):
    dp = [[0] * n for _ in range(m)]
    for row in range(m):
        for col in range(n):
            if row == 0 or col == 0:
                dp[row][col] = 1
            else:
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
    return dp[-1][-1]


if __name__ == '__main__':
    print(unique_path(3, 7))
    print(bottom_up_unique_path(3, 7))
