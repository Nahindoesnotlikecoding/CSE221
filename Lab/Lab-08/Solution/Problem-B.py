import sys
import heapq

def find_parent(node, parent):
    current = node
    while True:
        if current == parent[current]:
            return current
        else:
            current = parent[current]

def Problem_B():
    n, m = map(int, sys.stdin.readline().split())
    parent = []
    rank = []
    count = 0
    for i in range(n+1):
        parent.append(i)
        rank.append(1)
        
    heap = []
    for i in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        heapq.heappush(heap, (w, u, v))
    
    while heap:
        w, u, v = heapq.heappop(heap)
        parent_u = find_parent(u, parent)
        parent_v = find_parent(v, parent)
        if parent_u != parent_v:
            if rank[parent_u] >= rank[parent_v]:
                parent[parent_v] = parent_u
                rank[parent_u] += rank[parent_v]
            else:
                parent[parent_u] = parent_v
                rank[parent_v] += rank[parent_u]
            count += w
            
    print(count)

    
Problem_B()