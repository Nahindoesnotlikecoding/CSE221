import os, sys, ast, time, random, threading, subprocess
# Compile and run: pypy _A6D_Testing.py
def solve(N, R, edges):
    res = [0] * (N + 1)
    # your code here
    return  res



# stdin
# 4 1
# 3 1
# 4 1
# 1 2

# N, R = map(int, input().split())
# edges = []
# for i in range(N - 1):
#     u, v = map(int, input().split())
#     edges.append((u, v))

# # hardcoded input
N = 4
R = 1
edges = [(3, 1), (4, 1), (1, 2)]

start = time.time()
res = solve(N, R, edges)
finish = time.time()
elapsed = finish - start

# # file output
# with open("OutputOfYourCode.txt", "w") as fout:
#     fout.write(str(res))

# stdout
print(res)

print("Execution time for the targeted one test is " + f"{elapsed:.9f}" + "s", flush=True)
os._exit(0)