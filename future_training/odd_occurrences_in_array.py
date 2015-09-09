# https://codility.com/demo/take-sample-test/odd_occurrences_in_array/

from collections import defaultdict

def solution(A):
    count = defaultdict(int)
    for a in A:
        count[a] += 1    
    for value, occurrences in count.iteritems():
        if occurrences % 2 != 0:
            return value
