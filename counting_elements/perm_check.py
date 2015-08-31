# https://codility.com/demo/take-sample-test/perm_check/

def solution(A):
    N = len(A)
    elems = set()
    for a in A:
        if 0 < a < N + 1:
            elems.add(a)
    is_permutation = len(elems) == N
    return 1 if is_permutation else 0
