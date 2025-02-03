from collections import deque


def maxSlidingWindow(arr, k):
    dq = deque()
    result = []
    start = 0
    for index, value in enumerate(arr):
        window_size = index - k + 1
        if dq and dq[0] < window_size:
            dq.popleft()

        while dq and value > arr[dq[-1]]:
            dq.pop()
        dq.append(index)
        if index + 1 >= k:
            start += 1
            result.append(arr[dq[0]])

    return result


if __name__ == '__main__':
    print(maxSlidingWindow(arr=[4, 2, 12, 3, 8, 7, 6, 4, 3, 2], k=4))

# Input: nums = [1, 3, 1, 2, 0, 5], k = 3
# Input: nums = [4, 2, 12, 3, 8, 7, 6], k = 4
# Input: nums = [9, 7, 2, 4, 6, 8, 1], k = 2
