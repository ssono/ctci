import sys
sys.path.append("/home/ssono/projects/ctci/basics")

from structures.tree import *
from structures.linkedlist import *

"""
List of Depths:
Given a binary tree, design an algorithm that returns a linkedlist
of all nodes at depth D

returns a list of linkedlists by depth. root is at depth 0 in index 0
O(N) time and space
"""

def listByDepth(tree):
    l = []
    helper(l, tree.getRoot(), 0)
    return l

def helper(l, current, depth):
    if current == None:
        return
    if depth == len(l):
        newdepth = linkedList()
        l[depth] = newdepth
    l[depth].append(current)
    helper(l, current.getLeft(), depth + 1)
    helper(l, current.getRight(), depth + 1)
