def problem_C(t):
    x, y = t.split(" ")
    x, y = int(x), int(y)
    arr = input().split(" ")
    lst = []
    for i in range(len(arr)//2):
        temp = arr[i]
        arr[i] = arr[len(arr)-1-i]
        arr[len(arr)-1-i] = temp
        
    
    while y > 0:
        lst.append(arr[(len(arr)-y)])
        y -= 1
    print(" ".join(lst))
 
 
problem_C(input())