import sys
sys.path.append("/home/ssono/projects/ctci/basics")
from structures.linkedList import *

l1 = linkedList()
l1.append(7)
l1.append(1)
l1.append(6)
print(l1)

l2 = linkedList()
l2.append(5)
l2.append(9)
l2.append(2)
print(l2)

def sumLists(l1, l2):
    h1 = l1.getHead()
    h2 = l2.getHead()
    result = linkedList()
    newDigit = 0

    while(h1 != None and h2 != None):
        newDigit += h1.getData() + h2.getData()
        result.append(newDigit % 10)
        newDigit //= 10
        h1 = h1.getNext()
        h2 = h2.getNext()

    while(h1 != None):
        newDigit += h1.getData()
        result.append(newDigit % 10)
        newDigit //= 10
        h1 = h1.getNext()

    while(h2 != None):
        newDigit += h2.getData()
        result.append(newDigit % 10)
        newDigit //= 10
        h2 = h2.getNext()

    return result

print(sumLists(l1, l2))

#if lists are stored in descending order, use stacks to reverse and then do same as above
