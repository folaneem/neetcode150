def lengthOfLongestSubstring(s: str) -> int:
    storage = {}
    result = 0
    l = 0

    for index, value in enumerate(s):
        if value in storage:
            l = max(l, storage[value] + 1)
        storage[value] = index
        result = max(result, index - l + 1)

    return result


if __name__ == '__main__':
    print(lengthOfLongestSubstring(s="abba"))
