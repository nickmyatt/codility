# https://codility.com/demo/take-sample-test/tree_height

def height(tree):
    if tree is None:
        return -1
    else:
        return max(
            height(tree.l),
            height(tree.r),
        ) + 1

def solution(T):
    return height(T)
