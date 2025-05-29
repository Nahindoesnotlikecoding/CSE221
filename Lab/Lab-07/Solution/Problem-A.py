import sys
import heapq

def Problem_A():
    n, m, s, d = map(int, sys.stdin.readline().split())
    vertices = {}
    parent = {}
    dist_from_source = {}
    explored = {}
    for i in range(1, n+1):
        vertices.update({i: []})
        parent.update({i: None})
        dist_from_source.update({i: float('inf')})
        explored.update({i: False})
        
    u = list(map(int, sys.stdin.readline().split()))
    v = list(map(int, sys.stdin.readline().split()))
    w = list(map(int, sys.stdin.readline().split()))

    for i in range(len(u)):
        vertices[u[i]].append((v[i], w[i]))
    
    if s==d:
        print(0)
        print(s)
        return 
    
    dist_from_source[s] = 0
    heap = [(0, s)]
    while heap:
        u_dist, u_node = heapq.heappop(heap)
        explored[u_node] = True
        for v in vertices[u_node]:
            if not explored[v[0]]:
                if dist_from_source[u_node] + v[1] < dist_from_source[v[0]]:
                    dist_from_source[v[0]] = dist_from_source[u_node] + v[1]
                    parent[v[0]] = u_node
                    heapq.heappush(heap, (dist_from_source[v[0]], v[0]))

    path = []
    current = d
    while current != None:
        path.append(current)
        current = parent[current]
    
    if len(path) == 1:
        print(-1)
    else:
        print(dist_from_source[d])
        for i in range(len(path)-1, -1, -1):
            print(path[i], end=" ")
    
Problem_A()