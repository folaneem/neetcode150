def three_sums(nums):
    res = []
    nums.sort()

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        j = i + 1
        k = len(nums) - 1

        while j < k:
            num_i = nums[i]
            num_j = nums[j]
            num_k = nums[k]
            total = num_i + num_j + num_k

            if total > 0:
                k -= 1
            elif total < 0:
                j += 1
            else:
                res.append([num_i, num_j, num_k])
                j += 1

                while nums[j] == nums[j - 1] and j < k:
                    j += 1
    return res


if __name__ == '__main__':
    print(three_sums(nums=[1, 2, -2, -1, -1, 0, 0, 1, 2, -2, -1, 3, -3, 4, -4]))
