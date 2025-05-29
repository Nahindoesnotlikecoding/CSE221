import sys
sys.setrecursionlimit(2*1000000)

def find_parent(node, parent):
    while parent[node] != node:
        parent[node] = parent[parent[node]]
        node = parent[node]
    return node
def dfs(current, target, parent_node, max_edge, vertices):
    if current == target:
        return max_edge
    for neighbor, weight in vertices.get(current, []):
        if neighbor == parent_node:
            continue
        result = dfs(neighbor, target, current, max(max_edge, weight), vertices)
        if result != -1:
            return result
    return -1

def Problem_C():
    n, m = map(int, sys.stdin.readline().split())
    parent = []
    rank = []
    edges = []
    mst_edges = []
    not_used_edges = []
    min_cost = 0
    count = 0
    for i in range(n+1):
        parent.append(i)
        rank.append(1)

    for i in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((w, u, v))
    
    edges.sort()
    for i in edges:
        w, u, v,= i[0], i[1], i[2]
        parent_u = find_parent(u, parent)
        parent_v = find_parent(v, parent)
        if parent_u != parent_v:
            if rank[parent_u] >= rank[parent_v]:
                parent[parent_v] = parent_u
                rank[parent_u] += rank[parent_v]
            else:
                parent[parent_u] = parent_v
                rank[parent_v] += rank[parent_u]
            min_cost += w
            mst_edges.append((w, u, v))
            count += 1
        else:
            not_used_edges.append((w, u, v))
        
    
    if count!=n-1:
        print(-1)
        return
    
    vertices = {i: [] for i in range(1, n+1)}  
    for i in mst_edges:
        w, u, v= i[0], i[1], i[2]
        vertices[u].append((v, w))
        vertices[v].append((u, w))
    
    sec_min_cost = float('inf')
    for w_new, u_new, v_new in not_used_edges:
        max_path = dfs(u_new, v_new, -1, 0, vertices)
        if max_path >= w_new:
            continue
        
        candidate = min_cost - max_path + w_new
        if candidate > min_cost and candidate < sec_min_cost:
            sec_min_cost = candidate
    
    if sec_min_cost != float('inf'):
        print(sec_min_cost)
    else:
        print(-1)
    
Problem_C()