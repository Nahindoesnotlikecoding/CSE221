def problem_A(t):
    for i in range(t):
        inp = int(input())
        if inp%2==0:
            print(f"{inp} is an Even number.")
        else:
            print(f"{inp} is an Odd number.")
 
problem_A(int(input()))
