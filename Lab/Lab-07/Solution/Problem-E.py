import sys
import heapq

def Problem_E():
    n, m = map(int, sys.stdin.readline().split())
    vertices = {}
    dst_from_source = []
    for i in range(n+1):
        dst_from_source.append([float('inf'), float('inf')])

    for i in range(1, n+1):
        vertices.update({i: []})

    u = list(map(int, sys.stdin.readline().split()))
    v = list(map(int, sys.stdin.readline().split()))
    w = list(map(int, sys.stdin.readline().split()))

    for i in range(m):
        vertices[u[i]].append((v[i], w[i]))

    dst_from_source[1][0] = 0
    dst_from_source[1][1] = 0
    heap = [(0, 1, 0), (0, 1, 1)]
    while heap:
        u_dist, u_node, u_parity = heapq.heappop(heap)
        for v in vertices[u_node]:
            v_node, v_weight = v[0], v[1]
            if u_parity != v_weight%2:
                v_parity = 1-u_parity
                if dst_from_source[u_node][u_parity]+v_weight<dst_from_source[v_node][v_parity]:
                    dst_from_source[v_node][v_parity] = dst_from_source[u_node][u_parity]+v_weight
                    heapq.heappush(heap, (dst_from_source[v_node][v_parity], v_node, v_parity))
    
    
    if dst_from_source[n][0] == float('inf') and dst_from_source[n][1] == float('inf'):
        print(-1)
    else:
        print(min(dst_from_source[n][0], dst_from_source[n][1]))

Problem_E()