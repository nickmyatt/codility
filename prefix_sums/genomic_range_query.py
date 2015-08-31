# https://codility.com/demo/take-sample-test/genomic_range_query/

from collections import defaultdict

def solution(nucleotides, P, Q):
    nucleotides_to_factors = { "A" : 1, "C" : 2, "G" : 3, "T" : 4 }
    factors = [ nucleotides_to_factors[n] for n in nucleotides ]
    
    # We use the limited range of the data (only 4 values
    # G, T, A, C) to build an index of the last occurrences
    # of each of the factors, which can be used to anwer
    # each query in constant time.
    index = []
    last_seen = defaultdict(int)
    for pos, factor in enumerate(factors):
        last_seen[factor] = pos
        index.append(list(sorted(last_seen.items())))
    
    min_factors = [
        min(factor for factor, pos in index[end] if start <= pos)
        for start, end in zip(P, Q)
    ]
    
    return min_factors
