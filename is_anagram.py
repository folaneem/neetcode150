def is_anagram(s, t):
    return sorted(s) == sorted(t)


if __name__ == '__main__':
    print(is_anagram('cat', 'act'))
