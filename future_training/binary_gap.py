# https://codility.com/demo/take-sample-test/binary_gap/

from itertools import groupby

def solution(N):
    bits = bin(N)[2:]
    bit_runs = ( (bit, sum(1 for _ in grouper)) for bit, grouper in groupby(bits) )
    binary_gaps = [ length for bit, length in list(bit_runs)[1:-1] if bit == '0' ]
    return max(binary_gaps or [0])
