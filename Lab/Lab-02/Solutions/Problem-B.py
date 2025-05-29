import sys
def problem_B():
    n = int(sys.stdin.readline())
    arr1 = list(map(int, sys.stdin.readline().split(" ")))
    m = int(sys.stdin.readline())
    arr2 = list(map(int, sys.stdin.readline().split(" ")))
    new_arr = [0]*(len(arr1)+len(arr2))
    i = 0
    j = 0
    k = 0
    while i<len(arr1) and j<len(arr2):
        if arr1[i] < arr2[j]:
          new_arr[k] = arr1[i]
          i += 1
        else:
            new_arr[k] = arr2[j]
            j += 1
        k += 1
    
    while i<len(arr1):
        new_arr[k] = arr1[i]
        i+=1
        k+=1
    while j<len(arr2):
        new_arr[k] = arr2[j]
        j += 1
        k += 1
    
    for i in range(len(new_arr)):
        print(new_arr[i], end=" ")
 
 
problem_B()