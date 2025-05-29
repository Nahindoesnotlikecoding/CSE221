import sys
from collections import deque

def bfs(parent, color, vertices, s, d):
    if s==d:
        return [s]
    
    queue = deque()
    queue.append(s)
    color[s] = 1
    while queue:
        u = queue.popleft()
        for i in vertices[u]:
            if color[i] == 0:
                color[i] = 1
                queue.append(i)
                parent[i] = u

    path = shortest_path(parent, d)
    if path!=None:
        path.reverse()
        path.append(d)
        return path
    else:
        return None
        

def shortest_path(parent, d):
    path = []
    current = d
    while parent[current] != None:
        path.append(str(parent[current]))
        current = parent[current]
    
    if len(path)==0:
        return None
    return path

def problem_D():
    n, m, s, d, k = map(int, sys.stdin.readline().split())
    vertices = {}
    parent = {}
    color = {}
    for i in range(1, n+1):
        vertices.update({i: []})
        color.update({i: 0})
        parent.update({i: None})
    
    for i in range(m):
        u, v = map(int, sys.stdin.readline().split())
        vertices[u].append(v)
    
    if s==d and d==k:
        print(0)
        print(s)
        return
    
    for i in vertices:
        vertices[i].sort()
    
    parent2 = parent.copy()
    vertices2 = vertices.copy()
    color2 = color.copy()
    
    path1 = bfs(parent, color, vertices, s, k)
    path2 = bfs(parent2, color2, vertices2, k, d)
    
    if path1 == None or path2 == None:
        print(-1)
        return

    else:
        path = path1+path2[1:]
        print(len(path)-1)
        for i in range(len(path)):
            print(path[i], end=" ")
    

problem_D()