import sys
sys.path.append("/home/ssono/projects/ctci/basics")

from structures.lgraph import *
from structures.stack import *

"""route between nodes
design an algo to find whether there is a path between 2 nodes"""

#dfs
def DFS(g, start, end):
    visited = {}
    for n in g.getNodes():
        visited[n] = 0
    st = Stack()
    st.push(None)
    current = start
    while(not st.isEmpty()):
        if current == None:
            return False
        if current == end:
            return True
        visited[current] = 1
        end = True
        for n in current.getChildren():
            if visited[n] == 0:
                st.push(current)
                current = n
                done = False
        if done:
            current = st.pop()
    return False
