from collections import deque


def generate_parentheses_iterative(n):
    stack = [("", 0, 0)]  #
    result = []

    while len(stack) > 0:
        s, open_count, close_count = stack.pop()

        if len(s) == n * 2:
            result.append(s)
            continue

        if open_count < n:
            stack.append((s + '(', open_count + 1, close_count))

        if close_count < open_count:
            stack.append((s + ')', open_count, close_count + 1))

    return result


# Example usage
n = 3
print(generate_parentheses_iterative(n))
