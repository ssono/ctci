import sys
sys.path.append("/home/ssono/projects/ctci/basics")
from structures.linkedList import *

"""Partition:
write a function that takes as params a linked list and a number.
The output should be the linked list where all values less than the partition value
come before all the values greater than or equal to the partition val"""

l = linkedList()
l.add(1)
l.add(2)
l.add(10)
l.add(5)
l.add(8)
l.add(5)
l.add(3)
print(l)

#iterative rather than
def partition(l, number):
    greater = l.getHead()
    lesser = None

    while(True):
        while(greater.getData() < number):
            greater = greater.getNext()
            if greater == None:
                return l

        if lesser == None:
            lesser = greater

        while(lesser.getData() >= number):
            lesser = lesser.getNext()
            if lesser == None:
                return l

        temp = lesser.getData()
        lesser.setData(greater.getData())
        greater.setData(temp)
        print(l)

print(partition(l, 5))
