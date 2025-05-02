def solution(height):
    l, r = 0, len(height) - 1
    result = float("-inf")
    while l < r:
        lh = height[l]
        rh = height[r]

        area = lh * rh

        if lh > rh:
            r -= 1
        else:
            l += 1
        result = max(result, area)

    return result


if __name__ == "__main__":
    print(solution(height=[1, 7, 2, 5, 4, 7, 3, 6]))
