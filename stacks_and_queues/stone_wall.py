# https://codility.com/demo/take-sample-test/stone_wall/

def solution(heights):
    blocks = 0
    stack = [0]
    for height in heights:
        while stack[-1] > height:
            stack.pop()
            blocks += 1
        if stack[-1] < height:
            stack.append(height)
    blocks += len(stack) - 1
    return blocks
