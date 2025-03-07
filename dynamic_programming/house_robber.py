import math
from linecache import cache

from linked_list.reverse_linked_list import result


def top_bottom(nums):
    cache = {0: nums[0], 1: nums[1]}
    size = len(nums)

    def f(house):
        if house in cache:
            return cache.get(house)
        else:
            return f(house - 2) + nums[house]

    return f(size - 1)


def bottom_up(nums):
    size = len(nums)
    dp = [0] * (size + 1)
    dp[0] = nums[0]
    dp[1] = nums[1]

    for index in range(2, size):
        dp[index] = dp[index - 2] + nums[index]
    return max(dp)


if __name__ == '__main__':
    print(top_bottom(nums=[2, 7, 9, 3, 1]))
    print(bottom_up(nums=[2, 7, 9, 3, 1]))
