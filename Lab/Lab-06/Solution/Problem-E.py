import sys
from collections import deque

def bfs(vertices, color, distance, source):
    queue = deque()
    queue.append(source)
    color[source] = 1
    last_popped = None
    while queue:
        u = queue.popleft()
        last_popped = u
        for v in vertices[u]:
            if color[v] == 0:
                color[v] = 1
                distance[v] = distance[u]+1
                queue.append(v)

    return last_popped

def Problem_E():
    n = int(sys.stdin.readline())
    vertices = {}
    color = {}
    distance = {}
    for i in range(1, n+1):
        vertices.update({i: []})
        color.update({i: 0})
        distance.update({i: 0})
    
    random_point = 1
    for i in range(n-1):        
        u, v = map(int, sys.stdin.readline().split())
        if i == 0:
            random_point = u
        vertices[u].append(v)
        vertices[v].append(u)
    
    
    start_point = bfs(vertices, color, distance, random_point)

    color = {}
    distance = {}
    for i in range(1, n+1):
        color[i] = 0
        distance[i] = 0

    end_point = bfs(vertices, color, distance, start_point)
    
    print(distance[end_point])
    print(start_point, end_point)


Problem_E()