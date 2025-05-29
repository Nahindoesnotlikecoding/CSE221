import sys
def problem_D():
    n, m = map(int, sys.stdin.readline().split())
    odd_count = 0
    degree = [0]*(n+1)
    u = list(map(int, sys.stdin.readline().split()))
    v = list(map(int, sys.stdin.readline().split()))
    for i in range(m):
        degree[u[i]] += 1
        degree[v[i]] += 1
    
    for i in degree:
        if i%2!=0:
            odd_count += 1
    
    if odd_count==0 or odd_count==2:
        print("YES")
    else:
        print("NO")


problem_D()