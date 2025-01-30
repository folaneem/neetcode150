def solution(height):
    res = 0
    left, right = 0, len(height)-1
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        res = max(res, area)
        if height[left] < height[right]:
            left +=1
        elif height[right] <= height[left]:
            right -=1
    return res


if __name__ == "__main__":
    print(solution(height=[1,7,2,5,4,7,3,6]))