def problem_B():
    n, m = map(int, input().split(" "))
    u = list(map(int, input().split(" ")))
    v = list(map(int, input().split(" ")))
    w = list(map(int, input().split(" ")))
    matrix = {}
    for i in range(1, n+1):
        matrix.update({i: []})
    
    for i in range(m):
        matrix[u[i]].append((v[i], w[i]))
    
    for i in matrix.keys():
        if len(matrix[i])==0:
            print(f"{i}:")
        else:
            print(f"{i}:", end=" ")
        for j in matrix[i]:
            if matrix[i].index(j) == len(matrix[i])-1:
                print(j)
            else:
                print(j, end=" ")

problem_B()
