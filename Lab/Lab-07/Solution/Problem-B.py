import sys
import heapq

def dijkstra(vertices, parent, explored, dist_from_source, source):
    dist_from_source[source] = 0
    heap = [(0, source)]
    while heap:
        u_dist, u_node = heapq.heappop(heap)
        explored[u_node] = True
        for v in vertices[u_node]:
            if not explored[v[0]]:
                if dist_from_source[u_node] + v[1] < dist_from_source[v[0]]:
                    dist_from_source[v[0]] = dist_from_source[u_node] + v[1]
                    parent[v[0]] = u_node
                    heapq.heappush(heap, (dist_from_source[v[0]], v[0]))
    
    return dist_from_source, parent


def Problem_B():
    n, m, s, t = map(int, sys.stdin.readline().split())
    vertices = {}
    parent_s = [None]*(n+1)
    dist_from_source_s = [0]*(n+1)
    explored_s = [False]*(n+1)
    parent_t = [None]*(n+1)
    dist_from_source_t = [0]*(n+1)
    explored_t = [False]*(n+1)

    for i in range(1, n+1):
        vertices.update({i: []})
        dist_from_source_s[i] = float('inf')
        dist_from_source_t[i] = float('inf')
    
    for i in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        vertices[u].append((v, w))
    if s==t:
        print(0, s)
        return
    
    dst_from_src_s, parent_s = dijkstra(vertices, parent_s, explored_s, dist_from_source_s, s)
    dst_from_src_t, parent_t = dijkstra(vertices, parent_t, explored_t, dist_from_source_t, t)

    possible_nodes = []
    for i in range(1, len(dist_from_source_s)):
        if dist_from_source_s[i]!=float('inf') and dist_from_source_t[i]!=float('inf'):
            if i not in possible_nodes:
                possible_nodes.append(i)
    
    if len(possible_nodes) == 0:
        if dst_from_src_s[t] != float('inf') and dst_from_src_t[s] != float('inf'):
            if dst_from_src_s[t] < dst_from_src_t[s]:
                print(dst_from_src_s[t], t)
            else:
                print(dst_from_src_t[s], s)

        elif dst_from_src_s[t] == float('inf') and dst_from_src_t[s] != float('inf'):
            print(dst_from_src_t[s], s)
        elif dst_from_src_t[s] == float('inf') and dst_from_src_s[t] != float('inf'):
            print(dst_from_src_t[s], s)        
        elif dst_from_src_s[t] == float('inf') and dst_from_src_t[s] == float('inf'):
            print(-1)

    else:
        min = float('inf')
        min_node = None
        for i in possible_nodes:
            x = dst_from_src_s[i]
            y = dst_from_src_t[i]
            if max(x, y)<min:
                min = max(x, y)
                min_node = i
        print(min, min_node)

Problem_B()