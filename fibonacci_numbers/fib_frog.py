from itertools import takewhile

def fibs():
    f1, f2 = 1, 0
    while True:
        yield f1
        f1, f2 = f1 + f2, f1

def solution(A):

    # A         =      [0,  0,  0,  1,  1,  0,  1,  0,  0,  0]
    # allowed   = [ T,  F,  F,  F,  T,  T,  F,  T,  F,  F,  F,  T]
    # min_jumps = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  0]
    
    allowed = [True] + [ bool(a) for a in A ] + [True]
    min_jumps = [-1] * (len(allowed) - 1) + [0]

    for k in reversed(xrange(len(min_jumps) - 1)):
        if allowed[k]:
            max_distance = len(allowed) - k
            candidate_fibs = takewhile(lambda f: f < max_distance, fibs())
            next_jumps = [
                min_jumps[k + f]
                for f in candidate_fibs
                if allowed[k + f] and min_jumps[k + f] > -1
            ]
            if next_jumps:
                min_jumps[k] = 1 + min(next_jumps)

    return min_jumps[0]
