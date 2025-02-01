def maxSlidingWindow(nums, k):
    result = []
    for index, value in enumerate(nums):
        if len(nums) - index == k - 1:
            break
        result.append(max(nums[index: index + k]))
    return result


if __name__ == '__main__':
    print(maxSlidingWindow(nums=[1, 2, 1, 0, 4, 2, 6], k=3))
