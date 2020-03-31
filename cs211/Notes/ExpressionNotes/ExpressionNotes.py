"""
Week 3 - Thursday Notes
Live Coding Examples
"""

"""In class: Postfix, S-expressions"""


def eval_postfix(s: str) -> int:
    """Input should look like '5 3 + 4 *'
    Example: eval_postfix('5 3 + 4 *') -> 32
    """
    stack = []
    tokens=s.split()
    for i in tokens:
        if i.isnumeric():
            stack.append(int(i))
        elif i == "+":
            right = stack.pop()
            left = stack.pop()
            stack.append(left + right)
        elif i == "*":
            right = stack.pop()
            left = stack.pop()
            stack.append(left * right)
        elif i == "-":
            right = stack.pop()
            left = stack.pop()
            stack.append(left - right)
        elif i == "/":
            right = stack.pop()
            left = stack.pop()
            stack.append(left // right)

    return stack[0]


def eval_postfix_short(s: str) -> int:
    """Input should look like '5 3 + 4 *'
    Example: eval_postfix('5 3 + 4 *') -> 32
    """
    ops = {'+': lambda x, y: x + y,
           '*': lambda x, y: x * y,
           '-': lambda x, y: x - y,
           '/': lambda x, y: x // y}
    stack = []
    tokens=s.split()
    for i in tokens:
        if i.isnumeric():
            stack.append(int(i))
        elif i in ops:
            right = stack.pop()
            left = stack.pop()
            result = ops[i](left, right)
            stack.append(result)
    return stack[0]


print(eval_postfix("5 3 + 4 / 4 * 2 -"))

print(eval_postfix_short("5 3 + 4 / 4 * 2 -"))

f = lambda x : x + 1
print(f(20))


# 5 is an s-expression
# ['+' 5 4] is an s-expression
# ['+' ['-' 5 4] ['+' 3 7]] is a tree

def parse_postfix(s: str) -> list:
    """Input should look like '5 3 + 4 *'
    Example: parse_postfix('5 3 + 4 *') -> ['*', ['-', 5, 3], 4]
    """
    ops = {'+': lambda x, y: x + y,
           '*': lambda x, y: x * y,
           '-': lambda x, y: x - y,
           '/': lambda x, y: x // y}
    stack = []
    tokens = s.split()
    for i in tokens:
        if i.isnumeric():
            stack.append(int(i))
        elif i in ops:
            right = stack.pop()
            left = stack.pop()
            result = [i, left, right]
            stack.append(result)
    return stack[0]


print(parse_postfix('5 3 - 4 *'))


def eval_sexp(sexp: list) -> int:
    ops = {'+': lambda x, y: x + y,
           '*': lambda x, y: x * y,
           '-': lambda x, y: x - y,
           '/': lambda x, y: x // y}
    if isinstance(sexp, int):
        return sexp
    else:
        right = eval_sexp(sexp.pop())
        left = eval_sexp(sexp.pop())
        op = sexp.pop()
        result = ops[op](left, right)
        return result


print(eval_sexp(parse_postfix('5 3 - 4 *')))