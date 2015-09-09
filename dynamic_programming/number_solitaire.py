# https://codility.com/demo/take-sample-test/number_solitaire/

def solution(A):
    for k in reversed(xrange(len(A))):
        A[k] += max(A[k + 1:min(len(A), k + 7)] or [0])
    return A[0]
