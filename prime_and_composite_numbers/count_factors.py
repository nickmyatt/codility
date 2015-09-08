# https://codility.com/demo/take-sample-test/count_factors/

from math import sqrt

def solution(N):
    factors = 0
    sqrt_N = int(sqrt(N))
    for candidate in xrange(1, sqrt_N + 1):
        if N % candidate == 0:
            factors += 2
    if sqrt_N * sqrt_N == N:
        factors -= 1
    return factors
