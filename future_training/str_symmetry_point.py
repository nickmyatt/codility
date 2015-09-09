# https://codility.com/demo/take-sample-test/str_symmetry_point/

def solution(S):
    if len(S) % 2 == 0:
        # Odd-length strings cannot satisfy the property
        return -1
    else:
        mid = len(S) // 2
        for k in xrange(mid):
            if S[k] != S[-(k + 1)]:
                return -1
        return mid
