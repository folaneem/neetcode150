def daily_temp(temp):
    res = [0] * len(temp)
    stack = []
    for index, value in enumerate(temp):
        while stack and stack[-1][1] < value:
            stack_index, stack_value = stack.pop()
            res[stack_index] = index - stack_index
        stack.append((index, value))
    return res

if __name__ == '__main__':
    print(daily_temp(temp=[30, 38, 30, 36, 35, 40, 28]))
