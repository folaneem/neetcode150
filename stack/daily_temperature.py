def daily_temp(temp):
    res = [0] * len(temp)
    stack = []

    for index, value in enumerate(temp):
        while stack and value > stack[-1][0]:
            temp_stack, index_stack = stack.pop()
            res[index_stack] = (index - index_stack)
        stack.append([value, index])
    return res


if __name__ == '__main__':
    print(daily_temp(temp=[30,38,30,36,35,40,28]))