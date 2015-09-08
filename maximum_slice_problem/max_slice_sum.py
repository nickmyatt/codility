# https://codility.com/demo/take-sample-test/max_slice_sum/

def solution(A):
    max_sum = min(A)
    sum_ = 0
    for a in A:
        if sum_ > 0:
            sum_ += a
        else:
            sum_ = a
        max_sum = max(max_sum, sum_)
    return max_sum
