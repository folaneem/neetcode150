def solution(tokens):
    notations = ["*", "-", "+", "/"]
    stack = []
    result = 0
    for token in tokens:
        if token in notations:
            a = stack[-2]
            b = stack[-1]
            a, b = int(a), int(b)
            if token == "*":
                ans = a * b
            elif token == "+":
                ans = a + b
            elif token == "-":
                ans = a - b
            else:
                ans = int(a / b)
            stack.pop()
            stack.pop()
            stack.append(ans)
            result = ans
        else:
            stack.append(token)
            result = token
    return result


if __name__ == '__main__':
    print(solution(tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
