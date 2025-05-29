import sys
def problem_D():
    t = int(sys.stdin.readline())
    for i in range(t):
        arr = sys.stdin.readline().strip()
        if int(arr[0]) == "1":
            print(1)
        elif arr[len(arr)-1] == "0":
            print(-1)
        else:
            lo = 0
            hi = len(arr)-1
            first = -1
            while lo <= hi:
                mid = (lo+hi)//2
                if int(arr[mid]) == 1:
                    hi = mid-1
                    first = mid
                elif int(arr[mid])>1:
                    hi = mid-1
                elif int(arr[mid])<1:
                    lo = mid+1

            if first != -1:
                print(first+1)
            else:
                print(-1)
problem_D()