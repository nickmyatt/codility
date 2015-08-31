# https://codility.com/demo/take-sample-test/min_avg_two_slice/

# Key insight is that there must exist either a 2-slice or
# a 3-slice having the minimum average.
#
# Consider two slices P and Q separated by a slice R.
# The average <P+Q+R> can never be less than the smallest
# of <P>, <Q>, <R> individually. This argument applies for
# any choice of P, Q, R (including when they are empty).
# Thus we can always achieve at least the same average by
# subdivision of a slice, as long as it is possible to 
# subdivide into at least 2 elements. This reasoning
# terminates once a slice of size 3 is reached. By separate
# reasoning a 2-slice having smaller average is obviously
# possible. Therefore the minimal average belongs to either
# a 2-slice or a 3-slice.
#
# Having located the leftmost minimal average 2/3-slice ~S,
# to prove that there is no longer slice having the same
# average starting to the left, consider that to extend the
# slice to the left would require the existence of another
# 2/3-slice having smaller average, and ~S would no longer
# be the leftmost (contradiction).

def solution(A):

    pairs = [
        ((a + b) / 2.0, k)
        for k, (a, b) in enumerate(zip(A, A[1:]))
    ]

    triples = [
        ((a + b + c) / 3.0, k)
        for k, (a, b, c) in enumerate(zip(A, A[1:], A[2:]))
    ]
    
    _, start = min(pairs + triples)
    
    return start
