def find_min(nums):
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid
    return nums[l]


if __name__ == '__main__':
    print(find_min(nums=[3, 4, 5, 6, 0, 1, 2]))
