import sys
sys.setrecursionlimit(2*100000)

def dfs(vertices, color, stack, u):
    color[u] = 1
    for i in vertices[u]:
        if color[i]==0:
            x = dfs(vertices, color, stack, i)
            if x == False:
                return x
        elif color[i]==1:
            return False
    
    color[u] = 2
    stack.append(u)
    return True

def Problem_A():
    n, m = map(int, sys.stdin.readline().split())
    vertices = {}
    color = {}
    for i in range(1, n+1):
        vertices.update({i: []})
        color.update({i: 0})
    for i in range(m):
        u, v = map(int, sys.stdin.readline().split())
        vertices[u].append(v)
    
    stack = []
    for i in vertices:
        if color[i]==0:
            x = dfs(vertices, color, stack, i)
            if not x:
                print(-1)
                return
    
    for i in range(len(stack)-1, -1, -1):
        print(stack[i], end=" ")

Problem_A()
