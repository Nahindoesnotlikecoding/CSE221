def problem_A():
    n, m = map(int, input().split())
    parent = {}
    vertices = {}
    color = {}
    queue = []
    for i in range(1, n+1):
        vertices.update({i: []})
        color.update({i: 0})
        parent.update({i: None})
    
    for i in range(m):
        u, v = map(int, input().split())
        vertices[u].append(v)
        vertices[v].append(u)
        vertices[u].sort()
        vertices[v].sort()
    
    queue.append(list(vertices.keys())[0])
    color[queue[0]] = 1


    while len(queue)!=0:
        u = queue.pop(0)
        print(u, end=" ")
        for i in vertices[u]:
            if color[i] == 0:
                color[i] = 1
                queue.append(i)
    
problem_A()