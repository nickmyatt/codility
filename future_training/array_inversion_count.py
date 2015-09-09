# https://codility.com/demo/take-sample-test/array_inversion_count/

class BTree(object):
    
    def __init__(self, val):
        self.x = val
        self.size = 1
        self.l = self.r = None
    
    def insert(self, val):
        """Insert val and update sizes for all parents; O(log(N))"""
        parent = child = self
        while child:
            child.size += 1
            parent = child
            if val > child.x:
                child = child.r
            else:
                child = child.l
        child = BTree(val)
        if val > parent.x:
            parent.r = child
        else:
            parent.l = child

    def gt(self, val):
        """Number of elements in tree greater than val; O(log(N))"""
        gt = 0
        tree = self
        while tree:
            if val < tree.x:
               gt += 1 + (tree.r.size if tree.r else 0)
               tree = tree.l
            elif val > tree.x:
                tree = tree.r
            else:
                gt += tree.r.size if tree.r else 0
                break
        return gt


def solution(A):
    inversions = 0
    if len(A) > 0:
        tree = BTree(A[0])
        for a in A[1:]:
            inversions += tree.gt(a)
            tree.insert(a)
    return inversions
