import sys

def find_parent(node, parent):
    current = node
    while True:
        if current == parent[current]:
            return current
        else:
            current = parent[current]
        

def Problem_A():
    n, k = map(int, sys.stdin.readline().split())
    parent = []
    rank = []
    for i in range(n+1):
        parent.append(i)
        rank.append(1)
    
    for i in range(k):
        u, v = map(int, sys.stdin.readline().split())
        parent_u = find_parent(u, parent)
        parent_v = find_parent(v, parent)
        if parent_u != parent_v:
            if rank[parent_u] >= rank[parent_v]:
                rank[parent_u] += rank[parent_v]
                parent[parent_v] = parent_u
            else:
                rank[parent_v] += rank[parent_u]
                parent[parent_u] = parent_v
        
        parent_u = find_parent(u, parent)
        print(rank[parent_u])


Problem_A()
    