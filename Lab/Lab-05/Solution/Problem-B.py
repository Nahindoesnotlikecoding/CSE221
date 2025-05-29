import sys
sys.setrecursionlimit(2*100000)

def dfs(vertices, color, source):
    color[source] = 1
    for i in vertices[source]:
        if color[i] == 0:
            print(i, end=" ")
            dfs(vertices, color, i)
    
    color[source] = 2


def problem_B():
    n, m = map(int, sys.stdin.readline().split())
    u = list(map(int, sys.stdin.readline().split()))
    v = list(map(int, sys.stdin.readline().split()))
    color = {}
    vertices = {}
    for i in range(1, n+1):
        vertices.update({i: []})
        color.update({i: 0})
    for i in range(m):
        vertices[u[i]].append(v[i])
        vertices[v[i]].append(u[i])
        vertices[u[i]].sort()
        vertices[v[i]].sort()
    
    source = list(vertices.keys())[0]
    print(source, end=" ")
    dfs(vertices, color, source)

problem_B()