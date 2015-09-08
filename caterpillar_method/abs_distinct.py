# https://codility.com/demo/take-sample-test/abs_distinct/

from functools import partial
from operator import ge
from itertools import takewhile, groupby
from heapq import merge

def solution(A):
    nonpositive = partial(ge, 0)
    left  = takewhile(nonpositive, A)
    right = takewhile(nonpositive, (-a for a in reversed(A)))
    merged = merge(left, right)
    groups = groupby(merged)
    return sum(1 for g in groups)
