import sys
import heapq

def Problem_F():
    n, m, s, d = map(int, sys.stdin.readline().split())
    vertices = {}
    dist_from_source = {}
    for i in range(1, n+1):
        vertices.update({i: []})
        dist_from_source.update({i: [float('inf'), float('inf')]})
    
    for i in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        vertices[u].append((v, w))
        vertices[v].append((u, w))
    
    dist_from_source[s][0] = 0
    heap = [(0, s)]
    while heap:
        u_dist, u_node = heapq.heappop(heap)
        for v in vertices[u_node]:
            v_node, v_weight = v[0], v[1]
            
            if u_dist + v_weight < dist_from_source[v_node][0]:
                dist_from_source[v_node][1] = dist_from_source[v_node][0]
                dist_from_source[v_node][0] = u_dist + v_weight
                heapq.heappush(heap, (u_dist + v_weight, v_node))
            
            elif dist_from_source[v_node][0] < u_dist + v_weight < dist_from_source[v_node][1]:
                dist_from_source[v_node][1] = u_dist + v_weight
                heapq.heappush(heap, (u_dist + v_weight, v_node))
            else:
                continue
    
    if dist_from_source[d][1] == float('inf'):
        print(-1)
    else:
        print(dist_from_source[d][1])

Problem_F()
