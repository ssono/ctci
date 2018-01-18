import sys
sys.path.append("/home/ssono/projects/ctci/basics")
import math
from structures.tree import *
"""check balanced:
implement a function that checks if a binary tree is balanced.
Balanced: the heights of any 2 subtrees differ by no more than 1

Strategy: record depths of all terminating subtrees and any discrepancy returns false.
"""

def checkBalance(tree):
    listOfDepths = []
    findDepths(listOfDepths, tree.getRoot(), 1)
    small = min(listOfDepths)
    big = max(listOfDepths)
    if math.pow(small - big, 2) > 1:
        return False
    return True

def findDepths(l, current, depth):
    if current == None:
        l.append(depth - 1)
        return
    findDepths(l, current.getRight(), depth + 1)
    findDepths(l, current.getLeft(), depth + 1)
