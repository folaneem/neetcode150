
def solution(strs):
    storage = {}
    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word in storage:
            storage[sorted_word].append(word)
        else:
            storage[sorted_word] = [word]
    ans = []
    return list(storage.values())


if __name__ == '__main__':
    print(solution(["act", "pots", "tops", "cat", "stop", "hat"]))
