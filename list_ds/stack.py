# LIFO
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        self.stack.pop()


stack = Stack()
stack.push(5)
stack.push(7)
stack.push(6)
print(stack.stack)
stack.pop()
print(stack.stack)
