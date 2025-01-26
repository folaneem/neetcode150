def solution(numbers, target):
    storage = {}
    ans = []
    for index, num in enumerate(numbers):
        remainder = target - num
        if remainder in storage:
            ans.append(storage[remainder] + 1)
            ans.append(index + 1)
            break
        else:
            storage[num] = index
    return ans


if __name__ == '__main__':
    print(solution(numbers=[1, 2, 2, 3, 4], target=4))
