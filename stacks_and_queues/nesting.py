# https://codility.com/demo/take-sample-test/nesting/

def solution(chars):
    stack = []
    for c in chars:
        if stack and stack[-1] == '(' and c == ')':
            stack.pop()
        else:
            stack.append(c)
    return 0 if stack else 1
