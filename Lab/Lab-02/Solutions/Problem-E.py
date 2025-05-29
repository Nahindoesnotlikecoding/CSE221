def problem_E():
    t = list(map(int, input().split(" ")))
    n, q = t[0], t[1]
    arr = list(map(int, input().split(" ")))
    for i in range(q):
        inp = list(map(int, input().split(" ")))
        x, y = inp[0], inp[1]

        lo = 0
        hi = len(arr)-1
        index1 = None

        while lo <= hi:
            mid = (lo+hi)//2
            if arr[mid] >= x:
                hi = mid-1
                index1 = mid
            else:
                lo = mid+1
        lo = 0
        hi = len(arr)-1
        index2 = None
        while lo <= hi:
            mid = (lo+hi)//2
            if arr[mid]<=y:
                lo = mid+1
                index2 = mid
            else:
                hi = mid-1
        
        if index1 == None or index2==None or index1>index2:
            print(0) 
        else:
            print(index2-index1+1)
    
problem_E()
