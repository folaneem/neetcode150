class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            if self.minStack[-1] >= val:
                self.minStack.append(val)
            else:
                self.minStack.append(self.minStack[-1])
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)


minStack = MinStack()
minStack.push(1)
minStack.push(2)
minStack.push(3)
print(minStack.stack)
print(minStack.minStack)
print(minStack.top())
print(minStack.getMin())
minStack.pop()
print(minStack.stack)
print(minStack.minStack)
print(minStack.top())
print(minStack.getMin())
