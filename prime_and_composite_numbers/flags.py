# https://codility.com/demo/take-sample-test/flags/

from itertools import izip
from math import sqrt

def find_peaks(seq):
    triples = izip(seq, seq[1:], seq[2:])
    peaks = []
    for k, (left, middle, right) in enumerate(triples, 1):
        if left < middle > right:
            peaks.append(k)
    return peaks


def find_distances(sorted_seq):
    pairs = izip(sorted_seq, sorted_seq[1:])
    distances = []
    for left, right in pairs:
        distances.append(right - left)
    return distances


def placed_flags(distances, min_spacing):
    placed = 1
    distance = 0
    for d in distances:
        distance += d
        if distance >= min_spacing:
            placed += 1
            distance = 0
    return placed


def solution(seq):
    if len(seq) < 3:
        return 0
    else:
        peaks = find_peaks(seq)
        if len(peaks) < 2:
            return len(peaks)
        else:
            distances = find_distances(peaks)
            max_flags = min(len(peaks), int(sqrt(len(seq))) + 1)
            for flags in reversed(xrange(1, max_flags + 1)):
                if placed_flags(distances, flags) >= flags:
                    return flags
