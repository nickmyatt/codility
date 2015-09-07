from itertools import izip, islice

def mod_fib(p):
    m = 2 ** p
    f1, f2 = 1, 0
    while True:
        yield f1
        f1, f2 = ((f1 % m) + (f2 % m)) % m, f1

def solution(A, B):
    fibs = [ list(islice(mod_fib(p), 0, len(A) + 1)) for p in xrange(31) ]
    return [ fibs[p][n] for n, p in izip(A, B) ]
