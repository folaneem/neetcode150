from collections import Counter


def top_k_frequent(nums, k):
    storage = Counter(nums).most_common(k)
    ans = [c[0] for c in storage]
    return ans


if __name__ == '__main__':
    print(top_k_frequent([7,7], 2))
