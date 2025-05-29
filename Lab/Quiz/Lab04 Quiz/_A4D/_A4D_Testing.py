import os, sys, ast, time, random, threading, subprocess
# Compile and run: pypy _A4D_Testing.py
def solve(N, edges):
    res = True
    # your code here
    
    return res



# stdin
# 3 2
# 0 1
# 1 2

# N, M = map(int, input().split())
# edges = []
# for i in range(M):
#     u, v = map(int, input().split())
#     edges.append((u, v))

# # hardcoded input
N = 5
edges = [(0, 1), (0, 2), (0, 3), (2, 3), (2, 4), (3, 4)]

start = time.time()
res = solve(N, edges)
finish = time.time()
elapsed = finish - start

# # file output
# with open("OutputOfYourCode.txt", "w") as fout:
#     fout.write(str(res))

# stdout
print(res)

print("Execution time for the targeted one test is " + f"{elapsed:.9f}" + "s", flush=True)
os._exit(0)
