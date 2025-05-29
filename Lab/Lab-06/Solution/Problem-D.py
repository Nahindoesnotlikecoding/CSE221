import sys
sys.setrecursionlimit(2*100000+5)

def dfs(vertices, color, subtree, u):
    color[u] = 1
    for i in vertices[u]:
        if color[i] == 0:
            dfs(vertices, color, subtree, i)
    
    
    color[u] = 2
    for i in vertices[u]:
        subtree[u] += subtree[i]
    subtree[u] += 1
    return

def Problem_D():
    n, r = map(int, sys.stdin.readline().split())
    vertices = {}
    color = {}
    subtree = [0]*(n+1)
    vertices.update({r: []})
    color.update({r: 0})

    for i in range(1, n+1):
        if i == r:
            continue
        vertices.update({i: []})
        color.update({i: 0})

    for i in range(n-1):
        u, v = map(int, sys.stdin.readline().split())
        vertices[u].append(v)
        vertices[v].append(u)
    
    dfs(vertices, color, subtree, r)
    
    q = int(sys.stdin.readline())
    for i in range(q):
        x = int(sys.stdin.readline())
        print(subtree[x])
    
Problem_D()