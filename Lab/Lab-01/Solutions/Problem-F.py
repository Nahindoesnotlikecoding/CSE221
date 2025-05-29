def problem_F(t):
    inp1 = input().split(" ")
    for i in range(len(inp1)):
        inp1[i] = int(inp1[i])
    
    inp2 = input().split(" ")
    for i in range(len(inp2)):
        inp2[i] = int(inp2[i])
    
    min_swap = 0
    for i in range(len(inp2)):
        max_index = i
        flag = False
        for j in range(i+1, len(inp2)):
            if inp2[j] > inp2[max_index]:
                max_index = j
                flag = True
            elif inp2[j] == inp2[max_index]:
                if inp1[j] < inp1[max_index]:
                    max_index = j
                    flag = True
        if flag:
            inp2[i], inp2[max_index] = inp2[max_index], inp2[i]
            inp1[i], inp1[max_index] = inp1[max_index], inp1[i]
            min_swap += 1

        
    print("Minimum swaps:", min_swap)
    for i in range(len(inp1)):
        print(f"ID: {inp1[i]} Mark: {inp2[i]}")
    
problem_F(int(input()))
