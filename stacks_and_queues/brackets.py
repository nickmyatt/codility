# https://codility.com/demo/take-sample-test/brackets/

def solution(chars):
    brackets = { '[' : ']', '{' : '}', '(' : ')' }
    stack = []
    for c in chars:
        if stack and brackets.get(stack[-1]) == c:
            stack.pop()
        else:
            stack.append(c)
    return 0 if stack else 1
