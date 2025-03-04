from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache.get(key)

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            pass
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
