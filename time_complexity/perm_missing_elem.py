# https://codility.com/demo/take-sample-test/perm_missing_elem/

def solution(A):
    N = len(A)
    lo = 1        # Smallest element expected
    hi = N + 1    # Largest element expected
    elems = N + 1 # Number of elements expected
    expected_sum = (lo + hi) * elems // 2
    actual_sum = sum(A)
    missing_value = expected_sum - actual_sum
    return missing_value
