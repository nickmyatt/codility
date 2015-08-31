# https://codility.com/demo/take-sample-test/tape_equilibrium/

def solution(A):
    diff = sum(A[1:]) - A[0]
    min_diff = abs(diff)
    for a in A[1:-1]:
        diff -= 2 * a
        min_diff = min(min_diff, abs(diff))
    return min_diff
