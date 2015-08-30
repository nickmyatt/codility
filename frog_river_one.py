# https://codility.com/demo/take-sample-test/frog_river_one/

def solution(X, A):
    leaves = set()
    for k, a in enumerate(A):
        leaves.add(a)
        if len(leaves) == X:
            return k
    return -1
