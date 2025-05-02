def squares_of_sorted_array(n):
    result = []
    l, r = 0, len(n) - 1

    while l <= r:
        ls = n[l] ** 2
        rs = n[r] ** 2
        if rs > ls:
            result.append(rs)
            r -= 1
        else:
            result.append(ls)
            l += 1
    return result[::-1]


if __name__ == '__main__':
    print(squares_of_sorted_array(n=[-4, -1, 0, 3, 10]))
