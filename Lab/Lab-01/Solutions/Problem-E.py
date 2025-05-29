def problem_E(inp):
    lst = input().split(" ")
    
    for i in range(len(lst)):
        lst[i] = int(lst[i])

    
    for i in range(len(lst)):
        is_swapped = False
        for j in range(len(lst)-1-i):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp

                is_swapped = True
        
        if is_swapped != True:
            break
    
    for i in range(len(lst)):
        print(lst[i], end=" ")


problem_E(int(input()))