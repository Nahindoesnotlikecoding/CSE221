import sys
import heapq

def problem_D():
    n, m, s, d= map(int, sys.stdin.readline().split())
    weight = list(map(int, sys.stdin.readline().split()))
    vertices = {}
    dst_from_source = [float('inf')]*(n+1)
    explored = [False]*(n+1)
    for i in range(1, n+1):
        vertices.update({i: []})

    for i in range(m):
        u, v = map(int, sys.stdin.readline().split())
        vertices[u].append(v)
    
    if s==d:
        print(weight[s-1])
        return
    
    dst_from_source[s] = 0
    heap = [(0, s)]
    while heap:
        u_dist, u_node = heapq.heappop(heap)
        explored[u_node] = True
        for v_node in vertices[u_node]:
            if not explored[v_node]:
                if weight[u_node-1]+weight[v_node-1]<dst_from_source[v_node]:
                    dst_from_source[v_node] = weight[u_node-1]+weight[v_node-1]
                    weight[v_node-1] = weight[u_node-1]+weight[v_node-1]
                    heapq.heappush(heap, (dst_from_source[v_node], v_node))
    
    if dst_from_source[d]==float('inf'):
        print(-1)
    else:
        print(dst_from_source[d])

problem_D()