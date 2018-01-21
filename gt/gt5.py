import sys
sys.path.append("/home/ssono/projects/ctci/basics")
from structures.tree import *

"""Validate BST:
Implement a function that determines if a binary tree is a binary search tree.

Strat: convert to list and create through O(N) time and space
ideal = inorder traversal comparing to next O(N) time O(1) space. Need to keep track of last seen in recursive calls?
"""

def validate(tree):
    inorder = []
    listify(tree.getRoot(), inorder)
    for i in range(0, len(inorder - 2)):
        if inorder[i] > inorder[i + 1]:
            return False
    return True

def listify(current, inorder):
    if current.hasLeft():
        listify(current.getLeft(), inorder)
    l.append(current.getKey())
    if current.hasRight():
        listify(current.getRight(), inorder)
    
