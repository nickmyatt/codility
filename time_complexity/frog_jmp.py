# https://codility.com/demo/take-sample-test/frog_jmp/

def solution(location, target, jump_length):
    distance = target - location
    jumps = distance // jump_length
    return jumps + (1 if jumps * jump_length < distance else 0)
