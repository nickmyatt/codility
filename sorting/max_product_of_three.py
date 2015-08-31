# https://codility.com/demo/take-sample-test/max_product_of_three/

from heapq import nlargest, nsmallest
from itertools import combinations

def top_bottom_n(seq, n):
    if len(seq) > 2 * n:
        res = []
        res.extend(nlargest(n, seq))
        res.extend(nsmallest(n, seq))
        return res
    else:
        return seq

def solution(A):

    pos = []
    neg = []
    zero = []
    for a in A:
        if a > 0: pos.append(a)
        if a < 0: neg.append(a)
        if a == 0: zero.append(a)
    
    top_bottom_3 = lambda seq: top_bottom_n(seq, 3)
    operands = top_bottom_3(pos) + top_bottom_3(neg) + top_bottom_3(zero)
    
    return max( p * q * r for p, q, r in combinations(operands, 3) )
