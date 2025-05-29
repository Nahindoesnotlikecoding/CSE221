def problem_B(t):
    for i in range(t):
        inp = input().split(" ")
        if inp[2] == "+":
            print(float(round(int(inp[1])+int(inp[3]), 6)))
        elif inp[2] == "-":
            print(float(round(int(inp[1])-int(inp[3]), 6)))
        elif inp[2] == "*":
            print(float(round(int(inp[1])*int(inp[3]), 6)))
        elif inp[2] == "/":
            print(float(round(int(inp[1])/int(inp[3]), 6)))
 
problem_B(int(input()))