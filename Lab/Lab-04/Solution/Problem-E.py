def problem_E():
    n, m = map(int, input().split())
    in_degree = [0]*n
    out_degree = [0]*n
    u = list(map(int, input().split()))
    v = list(map(int, input().split()))

    for i in range(m):
        out_degree[u[i]-1] += 1
        in_degree[v[i]-1] += 1

    for i in range(len(in_degree)):
        print(in_degree[i]-out_degree[i], end=" ")

problem_E()