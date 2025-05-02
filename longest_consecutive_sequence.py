def longest_consecutive_sequence(nums):
    unique_nums = set(nums)

    result = 0

    for num in unique_nums:
        if num -1 not in unique_nums:
            l = 0
            next_num = num
            while next_num in unique_nums:
                l += 1
                next_num += 1
            result = max(result, l)
    return result


if __name__ == '__main__':
    nums = [2, 20, 21, 22, 23, 24, 25, 26, 27, 28, 4, 10, 3, 4, 5]
    print(longest_consecutive_sequence(nums=nums))
