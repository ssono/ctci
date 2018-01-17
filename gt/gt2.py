import sys
sys.path.append("/home/ssono/projects/ctci/basics")

from structures.tree import *

"""Given a sorted(increasing order) array with unique element,
 write an algo to create a binary search tree"""

def toTree(arr):
    tree = BST()
    if len(arr) == 0:
        return tree
    tree.setRoot(helper(arr, tree, 0, len(arr) - 1))
    return tree

def helper(arr, tree, lo, hi):
    newnode = None
    if lo > hi:
        return newnode
    mid = (lo + hi) //2
    newnode = TreeNode(arr[mid], arr[mid])
    newnode.setLeft(helper(arr, tree, lo, mid - 1))
    newnode.setRight(helper(arr, tree, mid + 1, hi))
    return newnode
