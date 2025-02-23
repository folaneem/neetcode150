def binary_search(nums, target):
    size = len(nums)
    l = 0
    r = size - 1
    while l <= r:
        mid = (l + r) // 2
        if target > nums[mid]:
            l = mid + 1
        elif target < nums[mid]:
            r = mid - 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    print(binary_search(nums=[-1, 0, 2, 4, 6, 8, 9], target=9))
