import os, sys, time, random, threading, subprocess
N, M = 0, 0
A, B = [], []
# Compile and run: pypy _A2B_Testing.py
def solve(N, A, M, B):
    res = []
    # Place your code here
    return res




# stdin
# 4
# 1 3 5 7
# 4
# 2 2 4 8
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))



# # hardcoded input
# N, M = 4, 4
# A = [1, 3, 5, 7]
# B = [2, 2, 4, 8]

start = time.time()
res = solve(N, A.copy(), M, B.copy())
finish = time.time()
elapsed = finish - start

# # stdout
# print(res)

print("Execution time for the targeted one test is " + f"{elapsed:.9f}" + "s", flush=True)
os._exit(0)
# # file input
# with open("TimeLimitExceeded.txt") as fin:
# with open("CustomTest.txt") as fin:
# with open("WrongAnswer.txt") as fin:
#     lines = fin.readlines()
#     N = int(lines[2].split(" ")[2])
#     A = list(map(int, lines[3][5:-2].split(", ")))
#     M = int(lines[4].split(" ")[2])
#     B = list(map(int, lines[5][5:-2].split(", ")))

# # file output
# with open("OutputOfYourCode.txt", "w") as fout:
#     fout.write(str(res))
