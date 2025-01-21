def two_integer_sum(nums, target):
    storage = {}
    ans = []
    for index, num in enumerate(nums):
        remainder = target - num
        if remainder in storage:
            ans.append(storage[remainder])
            ans.append(index)
            return ans
        else:
            storage[num] = index
    return ans


if __name__ == '__main__':
    print(two_integer_sum([5, 2, 3, 4, 4, 19, 10, 8, 9], 13))
