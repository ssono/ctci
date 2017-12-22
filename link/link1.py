import sys
sys.path.append("/home/ssono/projects/ctci/basics")
from structures.linkedList import *


"""Remove Dups:
write code to remove duplicates from an unsorted linkedList"""

l = linkedList()
l.add('a')
l.add('b')
l.add('a')
l.add('c')
l.add('c')
l.add('d')
l.add('e')
print(l)

def removeDup(l):
    seen = {}
    current = l.getHead()
    prev = None
    while(current != None):
        if current.getData() in seen.keys():
            current = current.getNext()
            prev.setNext(current)
        else:
            seen[current.getData()] = 1
            prev = current
            current = current.getNext()

removeDup(l)
print(l)
