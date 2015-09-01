# https://codility.com/demo/take-sample-test/fish/

def solution(sizes, directions):
    LEFT, RIGHT = 0, 1
    top = lambda s: s[-1]
    survivors = 0
    fishes = [[], []]
    for size, direction in zip(sizes, directions):
        fishes[direction].append(size)
        while fishes[LEFT] and fishes[RIGHT]:
            min(fishes, key=top).pop()
        survivors += len(fishes[LEFT])
        fishes[LEFT] = []
    survivors += len(fishes[RIGHT])
    return survivors
