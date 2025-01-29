def lengthOfLongestSubstring(s: str) -> int:
    storage = {}
    l = 0
    res = 0
    for index, t in enumerate(s):
        if t in storage:
            l = max(storage[t] + 1, l)
        storage[t] = index
        res = max(res, index - l + 1)
    return res


if __name__ == '__main__':
    print(lengthOfLongestSubstring(s="zxyzxyz"))
