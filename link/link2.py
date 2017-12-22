import sys
sys.path.append("/home/ssono/projects/ctci/basics")
from structures.linkedList import *

"""return kth elem from last"""

def kFromLast(lizt, k):
    current = lizt.getHead()
    count = 0
    node = None
    while count < k and current.getNext() != None:
        count += 1
        current = current.getNext()
    if count != k:
        return None
    node = lizt.getHead()
    while current.getNext() != None:
        current = current.getNext()
        node = node.getNext()
    return node
