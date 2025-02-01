from collections import Counter
import math


def minimum_window(s, t):
    t_counter = Counter(t)
    s_counter = Counter()
    need = len(t_counter)
    have = 0
    start = 0
    result = math.inf
    tracker = [0, 0]
    for index, value in enumerate(s):
        s_counter[value] = s_counter.get(value, 0) + 1
        if s_counter[value] == t_counter[value]:
            have += 1
        while have == need:
            s_counter[s[start]] -= 1
            if index - start + 1 < result:
                result = index - start + 1
                tracker = [start, index]
            if s_counter[s[start]] < t_counter[s[start]]:
                have -= 1
            start += 1
    if result == math.inf:
        return ""
    else:
        return s[tracker[0]: tracker[1]]


if __name__ == '__main__':
    print(minimum_window(s="aaaaaaaaaaaabbbbbcdd", t="abcdd"))
