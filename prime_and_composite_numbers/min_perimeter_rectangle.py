# https://codility.com/demo/take-sample-test/min_perimeter_rectangle/

from math import sqrt

def solution(area):
    for width in reversed(xrange(1, int(sqrt(area)) + 1)):
        height = area // width
        if width * height == area:
            perimeter = 2 * (width + height)
            return perimeter
