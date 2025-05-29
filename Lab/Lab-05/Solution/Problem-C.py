import sys
from collections import deque

def shortest_path(parent, d):
    path = []
    current = d
    while current != None:
        path.append(str(parent[current]))
        current = parent[current]
    
    if len(path)==1:
        print(-1)
    else:
        print(len(path)-1)
        for i in range(len(path)-2, -1, -1):
            print(path[i], end=" ")
        print(d)


def problem_C():
    n, m, s, d = map(int, sys.stdin.readline().split())
    
    parent = {}
    vertices = {}
    color = {}
    for i in range(1, n+1):
        vertices.update({i: []})
        color.update({i: 0})
        parent.update({i: None})
    
    u = list(map(int, sys.stdin.readline().split()))
    v = list(map(int, sys.stdin.readline().split()))

    if s == d:
        print(0)
        print(s)
        return

    for i in range(m):
        vertices[u[i]].append(v[i])
        vertices[v[i]].append(u[i])
    
    for i in vertices:
        vertices[i].sort()

    
    queue = deque()
    queue.append(s)
    color[queue[0]] = 1

    while queue:
        u = queue.popleft()
        for i in vertices[u]:
            if color[i]==0:
                color[i] = 1
                queue.append(i)
                parent[i] = u
    

    shortest_path(parent, d)
            
problem_C()
    