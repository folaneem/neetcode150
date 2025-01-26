def three_sums(nums):
    result = []
    storage = {}
    for index_i, i in enumerate(nums):
        remainder = 0 - i
        for index_j, j in enumerate(nums):
            if index_i == index_j:
                pass
            else:
                what_left = remainder - j
                if what_left == 0:
                    print('i=', i, 'j=', j, 'remainder=', remainder)
                else:
                    storage[(remainder, j)] = (index_i, index_j)
    return result


if __name__ == '__main__':
    print(three_sums(nums=[-1, 0, 1, 2, -1, -4]))
