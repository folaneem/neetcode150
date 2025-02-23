from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key, value, timestamp):
        item = self.store.get(key, [])
        item.append([value, timestamp])
        self.store[key] = item

    def get(self, key: str, timestamp: int):
        values = self.store.get(key, [])

        if not values:
            return ""

        l, r = 0, len(values) - 1
        ans = ""
        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] <= timestamp:
                ans = values[mid][0]
                l = mid + 1
            else:
                r = mid + 1
        return ans


if __name__ == '__main__':
    timeMap = TimeMap()
    timeMap.set("alice", "happy", 1)
    print(timeMap.get("alice", 1))
    print(timeMap.get("alice", 2))
    timeMap.set("alice", "sad", 3)
    print(timeMap.get("alice", 3))
