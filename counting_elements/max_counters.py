# https://codility.com/demo/take-sample-test/max_counters/

def solution(N, operations):
    MAX_COUNTER = N + 1
    counters = [0] * N
    max_ = 0
    min_ = 0
    for op in operations:
        if op == MAX_COUNTER:
            min_ = max_
        else:
            c = op - 1
            counters[c] = max(counters[c], min_)
            counters[c] += 1
            max_ = max(max_, counters[c])
    counters = [ max(c, min_) for c in counters ]
    return counters

def naive_solution(N, operations):
    MAX_COUNTER = N + 1
    counters = [0] * N
    for op in operations:
        if op == MAX_COUNTER:
            max_ = max(counters)
            counters = [max_] * N
        else:
            counters[op - 1] += 1
    return counters
