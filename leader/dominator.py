# https://codility.com/demo/take-sample-test/dominator/

def solution(A):
    candidate = None
    depth = 0
    for a in A:
        if depth > 0:
            if candidate == a:
                depth += 1
            else:
                depth -= 1
        else:
            candidate = a
            depth += 1
    count = sum( 1 for a in A if a == candidate )
    if count > len(A) // 2:
        return A.index(candidate)
    else:
        return -1
