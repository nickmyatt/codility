# https://codility.com/demo/take-sample-test/peaks/

from itertools import izip
from math import sqrt

def calc_prefix_peaks(seq):
    if len(seq) < 3:
        return []
    triples = izip(seq, seq[1:], seq[2:])
    res = [0]
    count = 0
    for l, peak, r in triples:
        if l < peak > r:
            count += 1
        res.append(count)
    res.append(count)
    return res

def calc_factors(n):
    res = set()
    for k in xrange(1, int(sqrt(n)) + 1):
        if n % k == 0:
            res.add(k)
            res.add(n // k)
    return res

def contains_peaks(start, end, prefix_peaks):
    if start > 0:
        return prefix_peaks[end] - prefix_peaks[start - 1]
    else:
        return prefix_peaks[end]

def subdivisions(n, factors):
    for factor in factors:
            yield [ 
                ( k * factor, (k + 1) * factor - 1 )
                for k in xrange(n // factor)
            ]

def solution(seq):


    
    factors = calc_factors(len(A))
    prefix_peaks = calc_prefix_peaks(A)
    
    best = 0
    
    for blocks in subdivisions(len(A), factors):
        
        if all(
            contains_peaks(start, end, prefix_peaks)
            for start, end in blocks
        ):
            best = max(best, len(blocks))
    
    return best
