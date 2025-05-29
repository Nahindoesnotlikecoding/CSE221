def problem_A():
    n, m = map(int, input().split(" "))
    matrix = [[0]*n for _ in range(n)]

    for i in range(m):
        u, v, w = map(int, input().split(" "))
        matrix[u-1][v-1] = w
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()

problem_A()
