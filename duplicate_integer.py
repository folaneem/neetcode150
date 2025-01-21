# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

nums = [1, 2, 3, 3]


def solution(nums):
    unique_nums = set(nums)
    return len(nums) == len(unique_nums)


if __name__ == '__main__':
    print(solution(nums))
