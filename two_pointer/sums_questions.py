def two_sum(nums, target):
    left, right = 0, len(nums) - 1

    while right > left:
        total = nums[right] + nums[left]
        if total > target:
            right -= 1
        elif total < target:
            left += 1
        else:
            break
    return [left, right]


def three_sums(nums):
    nums.sort()
    result = []
    for index, num in enumerate(nums):
        if index > 0 and nums[index - 1] == num:
            continue
        left = index + 1
        right = len(nums) - 1
        diff = 0 - num
        while right > left:
            right_number = nums[right]
            left_number = nums[left]
            total = right_number + left_number
            if total == diff:
                result.append([num, nums[left], nums[right]])
                right, left = right - 1, left + 1
                while nums[left] == nums[left - 1] and right > left:
                    left += 1
                while nums[right] == nums[right + 1] and right > left:
                    right -= 1
            elif total > diff:
                right -= 1
            else:
                left += 1
    return result


def four_sum(nums, target):
    nums.sort()
    size = len(nums)
    result = []
    for index1 in range(size):
        if index1 > 0 and nums[index1] == nums[index1 - 1]:
            continue
        for index2 in range(index1 + 1, size):
            if index2 > index1 + 1 and nums[index2] == nums[index2 - 1]:
                continue

            remainder = nums[index1] + nums[index2]

            left = index2 + 1
            right = size - 1

            while right > left:
                total = remainder + nums[left] + nums[right]
                if total == target:
                    result.append([nums[index1], nums[index2], nums[left], nums[right]])

                    left, right = left + 1, right - 1

                    while right > left and nums[left] == nums[left - 1]:
                        left += 1

                    while right > left and nums[right] == nums[right + 1]:
                        right -= 1

                elif total > target:
                    right -= 1
                else:
                    left += 1
    return result


if __name__ == '__main__':
    print(four_sum(nums=[1, 0, -1, 0, -2, 2], target=0))
    # print(three_sums(nums=[-1, 0, 1, 2, -1, -4]))
    # print(two_sum(nums=[2, 7, 11, 15, 15, 17, 20, 34], target=54))
