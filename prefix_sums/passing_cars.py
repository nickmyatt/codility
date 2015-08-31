# https://codility.com/demo/take-sample-test/passing_cars/

def solution(cars):
    eastbound = 0
    passing = 0
    for car in cars:
        if car == 0:
            # Travelling east
            eastbound += 1
        else:
            # Travelling west; will pass ever car
            # to the left which is travelling east
            passing += eastbound
        if passing > 10**9:
            return -1
    return passing
