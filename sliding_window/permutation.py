from collections import Counter
from itertools import permutations


def permutation(s1, s2):
    s2_counter = Counter()
    s1_counter = Counter(s1)
    start = 0
    for index, value in enumerate(s2):
        s2_counter[value] = s2_counter.get(value, 0) + 1
        if index > len(s1) - 1:
            if s2_counter[s2[start]] == 1:
                del s2_counter[s2[start]]
            else:
                s2_counter[s2[start]] -= 1
            start += 1
        print(s2_counter)
        if s1_counter == s2_counter:
            return True

    return False


if __name__ == '__main__':
    print(permutation(s1="abc", s2="llecabee"))
