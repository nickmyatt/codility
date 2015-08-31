# https://codility.com/demo/take-sample-test/count_div/

def count_lte(base, mod):
    """Number of positive integers less than or
    equal to `base` which are divisible by `mod`"""
    if base < 0:
        return 0
    else:
        # Extra 1 due to: 0 mod k = 1
        return 1 + base // mod

def solution(A, B, K):
    lte_B = count_lte(B, K)
    lt_A  = count_lte(A - 1, K)
    return lte_B - lt_A
