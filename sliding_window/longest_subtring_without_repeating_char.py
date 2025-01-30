def lengthOfLongestSubstring(s: str) -> int:
    start = 0
    result = 0
    for index, value in enumerate(s):
        while value in s[start: index]:
            start += 1
        result = max(result, index - start + 1)
    return result


if __name__ == '__main__':
    print(lengthOfLongestSubstring(s="au"))
