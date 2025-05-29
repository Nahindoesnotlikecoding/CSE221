import sys
def exponential(a, b, m):
    if b == 1:
        return a % m
    temp = exponential(a, b // 2, m)
    if b % 2 == 1:
        return (a * ((temp * temp) % m)) % m
    return (temp * temp) % m
 
def summation(a, n, m):
    if n == 1:
        return a % m
    else:
        if n % 2 == 0:
            temp = summation(a, n // 2, m)
            return (temp * (1 + exponential(a, n // 2, m))) % m
        else:
            temp = summation(a, n//2, m)
            return (temp * (1 + exponential(a, n//2, m)) + exponential(a, n, m)) % m
def solve():
    t = int(sys.stdin.readline())
    for i in range(t):
        a, n, m = map(int, sys.stdin.readline().split(" "))
        res = summation(a, n, m)
        print(res)
 
solve()