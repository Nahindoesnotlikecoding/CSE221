def problem_C():
    n = int(input())
    matrix = [[0]*n for i in range(n)]
    for i in range(n):
        inp = list(map(int, input().split(" ")))
        for j in range(1, len(inp)):
            matrix[i][inp[j]] = 1
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()

problem_C()