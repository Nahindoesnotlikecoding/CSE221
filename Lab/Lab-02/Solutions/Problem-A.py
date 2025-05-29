def problem_A():
    t = list(map(int, input().split(" ")))
    arr = list(map(int, input().split(" ")))
    i = 0
    j = len(arr)-1
    while i<j:
        if arr[i]+arr[j]==t[1]:
            print(i+1, j+1)
            return 
        elif arr[i]+arr[j]<t[1]:
            i += 1
        elif arr[i]+arr[j]>t[1]:
            j -= 1
    print(-1)

problem_A()