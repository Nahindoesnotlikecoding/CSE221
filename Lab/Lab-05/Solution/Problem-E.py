import sys
sys.setrecursionlimit(2*100000+10)

def dfs(vertices, s):
    global hasCycle, color
    
    if hasCycle:
        return
    
    color[s] = 1
    for i in vertices[s]:
        if color[i]==0:
            color[i] = 1
            dfs(vertices, i)
        elif color[i] == 1:
            hasCycle = True
    
    color[s] = 2
    return hasCycle

def problem_E():
    global hasCycle, color
    n, m = map(int, sys.stdin.readline().split())
    vertices = {}
    color = {}
    hasCycle = False

    for i in range(1, n+1):
        vertices.update({i: []})
        color.update({i: 0})
    
    for i in range(m):
        u, v = map(int, sys.stdin.readline().split())
        vertices[u].append(v)
    
    for i in vertices:
        if color[i]==0:
            dfs(vertices, i)
    
    if hasCycle:
        print("YES")
    else:
        print("NO")
    
problem_E()