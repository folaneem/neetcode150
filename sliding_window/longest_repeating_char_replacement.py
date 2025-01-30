def characterReplacement(s, k):
    counter = {}
    result = 0
    start = 0
    for index, value in enumerate(s):
        counter[value] = counter.get(value, 0) + 1
        while index - start + 1 - max(counter.values()) > k:
            counter[s[start]] -= 1
            start += 1
        result = max(result, index - start + 1)
    return result


if __name__ == '__main__':
    print(characterReplacement(s="AAABABB", k=1))
