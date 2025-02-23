def car_fleet(target, speed, position):
    pair = [[p, s] for p, s in zip(position, speed)]
    stack = []
    for p, s in sorted(pair)[::-1]:
        time = 1 / s * (target - p)
        stack.append(time)
        if len(stack) >= 2 and time <= stack[-1]:
            stack.pop()
    return len(stack)


if __name__ == '__main__':
    print(car_fleet(target=10, position=[1, 4], speed=[3, 2]))
