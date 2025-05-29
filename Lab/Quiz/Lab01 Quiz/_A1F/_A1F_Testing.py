import os, sys, time, random, threading, subprocess

# Compile and run: pypy _A1F_Testing.py
def solve(sIDs, sMarks):
    N = len(sIDs)
    cnt = 0
    arr = []
    # Place your code here
    return (cnt, arr)

N = 0
sIDs, sMarks, res = [], [], []

# stdin
# 7
# 7 4 9 3 2 5 1
# 40 50 50 20 10 10 10
N = int(input())
sIDs = list(map(int, input().split()))
sMarks = list(map(int, input().split()))

start = time.time()
res = solve(sIDs.copy(), sMarks.copy())
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
#     sIDs = list(map(int, fin.readlines()[3][8:-2].split(", ")))
#     sMarks = list(map(int, fin.readlines()[3][10:-2].split(", ")))

# # hardcoded input
# sIDs = [7, 4, 9, 3, 2, 5, 1]
# sMarks = [40, 50, 50, 20, 10, 10, 10]


# # file output
# with open("OutputOfYourCode.txt", "w") as fout:
#     fout.write(str(res))