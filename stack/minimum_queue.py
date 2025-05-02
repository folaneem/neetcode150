from collections import deque


class MinQueue:
    def __init__(self):
        self.queue = deque()
        self.minQueue = deque()  # Stores elements in non-increasing order

    def enqueue(self, val: int) -> None:
        # Add value to the main queue
        self.queue.append(val)

        # Update the minQueue
        while self.minQueue and self.minQueue[-1] > val:
            self.minQueue.pop()
        self.minQueue.append(val)

    def dequeue(self) -> None:
        if not self.queue:
            raise IndexError("Dequeue from an empty queue")

        # If the front of both queues is the same, remove from minQueue as well
        if self.queue[0] == self.minQueue[0]:
            self.minQueue.popleft()

        self.queue.popleft()

    def front(self) -> int:
        if not self.queue:
            raise IndexError("Queue is empty")
        return self.queue[0]

    def getMin(self) -> int:
        if not self.minQueue:
            raise IndexError("Queue is empty")
        return self.minQueue[0]


q = MinQueue()

q.enqueue(5)
q.enqueue(3)
q.enqueue(7)
print(q.getMin())  # Output: 3

q.dequeue()
print(q.getMin())  # Output: 3

q.dequeue()
print(q.getMin())  # Output: 7
