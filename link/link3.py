import sys
sys.path.append("/home/ssono/projects/ctci/basics")
from structures.linkedList import *

"""Delete middle Node:
given access to a node in the middle of a linked list"""

#cascade valuse backwards and delete last
def deleteMid(node):
    while(node.getNext().getNext() != None):
        node.setData(node.getNext().getData())
        node = node.getNext()
    node.setData(node.getNext().getData())
    node.setNext(None)

l = linkedList()
l.add('e')
l.add('d')
l.add('c')
l.add('b')
l.add('a')
node = l.search('c')
print(l)
print(node)
deleteMid(node)
print(l)
