# https://codility.com/demo/take-sample-test/missing_integer/

def solution(A):
    """The largest possible covering with N values is the range
    1..N. Therefore we need only recall the presence of 1..N+1
    values. The first remaining gap in this sequence is the
    smallest missing value."""
    MIN = 0
    MAX = len(A) + 1
    seen_values = [True] + ([False] * MAX)
    for a in A:
        if MIN < a < MAX:
            seen_values[a] = True
    return min( k for k, seen in enumerate(seen_values) if not seen )
