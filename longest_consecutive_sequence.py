def longest_consecutive_sequence(nums):
    nums = sorted(set(nums))
    if len(nums) == 1:
        return 1
    print(nums)
    counter = 1
    result = 0
    for index, num in enumerate(nums):
        if index == 0:
            continue
        else:
            to_be_subtracted = nums[index - 1]
            if num - to_be_subtracted == 1:
                counter += 1
            else:
                counter = 1
        result = max(counter, result)
    return result


if __name__ == '__main__':
    nums = [2, 20, 21, 22, 23, 24, 25, 26, 27, 28, 4, 10, 3, 4, 5]
    print(longest_consecutive_sequence(nums=[0, 1]))
