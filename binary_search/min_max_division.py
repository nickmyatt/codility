# https://codility.com/demo/take-sample-test/min_max_division/

from bisect import bisect

def solution(K, M, A):
    
    if K >= len(A):
        return max(A)
    
    prefix = [0]
    for a in A:
        prefix.append(a + prefix[-1])
    
    AVG_BLOCK_SUM = prefix[-1] / float(K)
    
    def block_sum(slice_):
        return prefix[slice_.stop] - prefix[slice_.start]
        
    large_sum = 0
    start = stop = 0
    for k in xrange(1, K + 1):
        stop = bisect(prefix, AVG_BLOCK_SUM * k) - 1
        if stop == start:
            stop = min(start + 1, len(A))
        large_sum = max(large_sum, block_sum(slice(start, stop)))
        start = stop
    
    return large_sum
