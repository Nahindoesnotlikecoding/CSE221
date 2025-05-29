def problem_G(t):
    arr = []
    for i in range(t):
        inp = input().split(" ")
        temp = [inp[0], inp[6], inp[4]]
        arr.append(temp)
    
    for i in range(t):
        for j in range(t-1-i):
            if arr[j][0] == arr[j+1][0]:
                x1 = arr[j][1].split(":")
                x2 = arr[j+1][1].split(":")
                y1 = (int(x1[0])*60) + int(x1[1])
                y2 = (int(x2[0])*60) + int(x2[1])
                if y1 < y2:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            elif arr[j][0] > arr[j+1][0]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    for i in range(len(arr)):
        print(f"{arr[i][0]} will departure for {arr[i][2]} at {arr[i][1]}")

problem_G(int(input()))