import sys
import heapq

def Problem_C():
    n, m = map(int, sys.stdin.readline().split())
    vertices = {}
    explored = [0]*(n+1)
    danger = [float('inf')]*(n+1)

    for i in range(1, n+1):
        vertices.update({i: []})
    
    for i in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        vertices[u].append((v, w))
        vertices[v].append((u, w))
    
    danger[1] = 0
    heap = [(0, 1)]
    while heap:
        u_dist, u_node = heapq.heappop(heap)
        explored[u_node] = True
        for v in vertices[u_node]:
            v_node, v_weight = v[0], v[1]
            if not explored[v_node]:
                if max(danger[u_node], v_weight) < danger[v_node]:
                    danger[v_node] = max(danger[u_node], v_weight)
                    heapq.heappush(heap, (danger[v_node], v_node))

    
    for i in range(1, len(danger)):
        if danger[i] == float('inf'):
            print(-1, end=" ")
        else:
            print(danger[i], end=" ")


Problem_C()