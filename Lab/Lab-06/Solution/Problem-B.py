import sys
from collections import deque

def problem_B():
    n, m = map(int, sys.stdin.readline().split())
    vertices = {}
    color = {}
    for i in range(1, n+1):
        vertices.update({i: []})
        color.update({i: None})
    
    for i in range(m):
        u, v = map(int, sys.stdin.readline().split())
        vertices[u].append(v)
        vertices[v].append(u)
    
    ans = 0
    queue = deque()
    for i in vertices:
        c0, c1 = 0, 0
        if color[i] == None:
            for k in vertices[i]:
                if color[k] == 1:
                    color[i] = 0
                    c0 += 1
                    break
                elif color[k] == 0:
                    color[i] = 1
                    c1 += 1
                    break
                else:
                    continue
            if color[i] == None:
                color[i] = 0
                c0 += 1
            queue.append(i)

        # else:
        #     queue.append(i)
        while queue:
            u = queue.popleft()
            for j in vertices[u]:
                if color[j]==None:
                    color[j] = 1-color[u]
                    queue.append(j)
                    if color[j] == 1:
                        c1+= 1
                    else:
                        c0 += 1
                elif color[j] == color[u]:
                    print(max(c0, c1))
                    return
        ans += max(c0, c1)

    print(ans)

problem_B()
                        