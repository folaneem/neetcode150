def is_valid_parentheses(s):
    mapper = {')': '(', ']': '[', '}': '{'}
    stack = []
    for value in s:
        if value in mapper:
            if stack and stack[-1] == value:
                stack.pop()
        else:
            stack.append(value)
    if not stack:
        return True
    return False
if __name__ == '__main__':
    print(is_valid_parentheses(s="[(]"))
