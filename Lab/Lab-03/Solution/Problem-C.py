def exponential(a, b):
    if b == 1:
        return a
    else:
        temp = exponential(a, b//2)
        if b%2==0:
            return (temp*temp)%107
        else:
            return (a*temp*temp)%107


def problem_C():
    arr = input().split(" ")
    a, b = int(arr[0]), int(arr[1])
    c = exponential(a, b)

    print(c)
  
problem_C()