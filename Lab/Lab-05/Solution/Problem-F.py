import sys
from collections import deque


def bfs(vertices, source):
    global matrix, color

    diamond_count = 0
    if matrix[source] != "#":
        if matrix[source]=="D":
            diamond_count += 1  
        color[source] = 1
        queue = deque()
        queue.append(source)
        while queue:
            u = queue.popleft()
            for i in vertices[u]:
                if color[i] == 0:
                    color[i]=1
                    queue.append(i)
                    if matrix[i] == "D":
                        diamond_count += 1

    return diamond_count
        
        
def problem_F():
    global matrix, color
    r, h = map(int, sys.stdin.readline().split())
    n = r*h
    vertices = {}
    matrix = [0]*(r*h)
    color = {}
    
    for i in range(n):
        color.update({i: 0})
        vertices.update({i: []})
    
    count = 0
    for i in range(r):
        inp = list(sys.stdin.readline().strip())
        for j in range(len(inp)):
            matrix[count] = inp[j]
            count += 1
    
    for i in range(len(matrix)):
        on_left = False
        on_right = False
        on_up = False
        on_down = False
        
        if i%h!=0:
            on_left = True
        if (i%h)!=(h-1):
            on_right = True
        if i-h>=0:
            on_up =True
        if i+h<=(len(matrix)-1):
            on_down = True
        
        if on_left:
            if matrix[i-1]!="#":
                vertices[i].append(i-1)
        if on_right:
            if matrix[i+1]!="#":
                vertices[i].append(i+1)
        if on_down:
            if matrix[i+h]!="#":
                vertices[i].append(i+h)
        if on_up:
            if matrix[i-h]!="#":
                vertices[i].append(i-h)
    
    max_diamond = 0
    for i in range(len(matrix)):
        if color[i]==0:
            diamond_count = bfs(vertices, i)
            max_diamond = max(max_diamond, diamond_count)

    print(max_diamond)


problem_F()