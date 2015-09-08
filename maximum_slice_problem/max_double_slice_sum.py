# https://codility.com/demo/take-sample-test/max_double_slice_sum/

def reversal(f, A):
    return list(reversed(f(list(reversed(A)))))

def running_slices(A):
    res = []
    sum_ = 0
    start = 0
    for end, a in enumerate(A):
        if sum_ > 0:
            sum_ += a
        else:
            sum_ = a
        res.append((start, end, sum_))
    return res

def solution(A):
    ending_on = running_slices(A[1:-1])
    starting_on = reversal(running_slices, A[1:-1])

    start, end, best = max(ending_on, key=lambda t: t[2])
    element_to_remove = min(A[start:end + 1])
    best_single_slice = best - element_to_remove
    
    best_double_slice = 0
    for left_slice in ending_on:
        start, end, left_best = left_slice
        if end + 2 < len(starting_on):
            right_slice = starting_on[end + 2]
            _, _, right_best = right_slice
            best_double_slice = max(best_double_slice, left_best + right_best)
    
    return max(best_single_slice, best_double_slice)
