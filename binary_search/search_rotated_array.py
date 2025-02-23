def search(nums, target):
    l, r = 0, len(nums) - 1

    while l < r:
        mid = (l + r) // 2
        if nums[mid] > nums[l]:
            l = mid + 1
        else:
            r = mid
    min_index = l

    if min_index == 0:
        l, r = 0, len(nums) - 1
    elif target >= nums[min_index] and target <= nums[-1]:
        l, r = min_index, len(nums) - 1
    else:
        l, r = 0, min_index

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
    print(search(nums=[3, 4, 5, 6, -1, 0, 1, 2], target=5))
