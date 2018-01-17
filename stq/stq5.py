"""sorted stack:
write a program to sort a stack such that the smallest items are on top.
Use a temp stack.
stacks have push, pop, peek, isempty"""

import sys
import
sys.path.append("/home/ssono/projects/ctci/basics")
from structures.stack import *

def sortStack(original):
    reverse = Stack()
    while(!original.isEmpty()):
        if reverse.isEmpty():
            reverse.push(original.pop())
        else:
            temp = original.pop()
            while temp < reverse.peek() and !reverse.isEmpty():
                original.push(reverse.pop())
            reverse.push(temp)
    while !reverse.isEmpty():
        original.push(reverse.pop())
    return original
