import os, sys, ast, time, random, threading, subprocess
# Compile and run: pypy _A6C_Testing.py
def solve(N, X1, Y1, X2, Y2):
    res = 0
    # your code here
    return  res


# stdin
# 4
# 1 1
# 3 4

# N = int(input())
# X1, Y1 = list(map(int, input().split()))
# X2, Y2 = list(map(int, input().split()))

# # hardcoded input
N = 4
X1, Y1 = 1, 1
X2, Y2 = 3, 4

start = time.time()
res = solve(N, X1, Y1, X2, Y2)
finish = time.time()
elapsed = finish - start

# # file output
# with open("OutputOfYourCode.txt", "w") as fout:
#     fout.write(str(res))

# stdout
print(res)

print("Execution time for the targeted one test is " + f"{elapsed:.9f}" + "s", flush=True)
os._exit(0)