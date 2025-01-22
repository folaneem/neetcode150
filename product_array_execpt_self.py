import math


def solution(nums):
    result = []
    for index, num in enumerate(nums):
        other_nums = nums[:index] + nums[index + 1:]
        ans = math.prod(other_nums)
        result.append(ans)

    return result


if __name__ == '__main__':
    print(solution([-1,0,1,2,3]))
