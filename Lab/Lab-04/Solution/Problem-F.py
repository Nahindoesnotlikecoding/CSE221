def problem_F():
    n = int(input())
    x, y = map(int, input().split())
    moves = [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]
    valid_moves = []
    for i in moves:
        if n>=i[0]>0 and n>=i[1]>0:
            valid_moves.append(i)
    valid_moves.sort()
    print(len(valid_moves))
    for i in valid_moves:
        print(i[0], i[1])

problem_F()