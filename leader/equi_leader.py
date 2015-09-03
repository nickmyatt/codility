# https://codility.com/demo/take-sample-test/equi_leader/

from collections import defaultdict

def prefix_leader(seq):
    occurrences = defaultdict(int)
    leaders = []
    candidate = None
    depth = 0
    for length, elem in enumerate(seq, 1):
        if depth > 0:
            if elem == candidate:
                depth += 1
            else:
                depth -= 1
        else:
            candidate = elem
            depth = 1
        occurrences[elem] += 1
        if occurrences[candidate] > length // 2:
            leaders.append(candidate)
        else:
            leaders.append(None)
    return leaders

def solution(A):
    left_leaders = prefix_leader(A)
    right_leaders = list(reversed(prefix_leader(reversed(A))))[1:]
    equi_leaders = 0
    for l, r in zip(left_leaders, right_leaders):
        if l is not None and r is not None and l == r:
            equi_leaders += 1
    return equi_leaders
