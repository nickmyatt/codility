# https://codility.com/demo/take-sample-test/tie_ropes/

def solution(K, A):
    segments = 0
    length = 0
    for a in A:
        if length < K:
            length += a
        else:
            segments += 1
            length = a
    if length >= K:
        segments += 1
    return segments
