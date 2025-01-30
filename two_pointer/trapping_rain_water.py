def trap(heights):
    left, right = 0, len(heights) - 1
    water_trapped = 0
    max_left_height, max_right_height = 0, 0
    while left < right:
        left_height = heights[left]
        right_height = heights[right]

        if left_height >= right_height:
            trapped = max_right_height - right_height
            if trapped > 0:
                water_trapped += trapped
            if right_height >= max_right_height:
                max_right_height = right_height
            right -= 1
            pass
        else:
            trapped = max_left_height - left_height
            if trapped > 0:
                water_trapped += trapped
            if left_height >= max_left_height:
                max_left_height = left_height
            left += 1
            pass
    return water_trapped


if __name__ == '__main__':
    print(trap(heights=[0, 2, 0, 3, 1, 0, 1, 3, 2, 1]))
    print(trap(heights=[4, 2, 0, 3, 2, 5]))
    print(trap(heights=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
