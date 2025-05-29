import math
def problem_G():
    n, q = map(int, input().split())
    graph = [[] for i in range(n)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j:
                if math.gcd(i, j) == 1:
                    graph[i-1].append(j)
    for i in range(q):
        x, k = map(int, input().split())
        if len(graph[x-1]) >= k:
            print(graph[x-1][k-1])
        else:
            print(-1)
        
problem_G()