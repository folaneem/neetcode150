def min_eating_banana(piles, h):
    ans = max(piles)
    l = 1
    r = max(piles)
    while l <= r:
        mid = (l + r) // 2
        hours = calculate_hours(piles, mid)
        if hours > h:
            l = mid + 1
        else:
            ans = min(ans, mid)
            r = mid - 1
    return ans


def calculate_hours(piles, mid):
    hours = 0
    for v in piles:
        y = v // mid
        remainder = v % mid
        hours += y
        if remainder != 0:
            hours += 1
    return hours


# print(calculate_hours(piles=[1, 4, 5, 3, 2], mid=2))
print(min_eating_banana(piles=[25,10,23,4], h=4))
