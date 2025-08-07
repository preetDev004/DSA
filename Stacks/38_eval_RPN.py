from typing import List


def evalRPN(tokens: List[str]) -> int:
    op = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: int(x / y),
    }
    stack = []
    for i in tokens:
        if i in op and len(stack) >= 2:
            y = stack.pop()
            x = stack.pop()
            stack.append(op[i](x, y))
        else:
            stack.append(int(i))
    return stack[0]


print(evalRPN(["2", "1", "+", "3", "*"]))
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
