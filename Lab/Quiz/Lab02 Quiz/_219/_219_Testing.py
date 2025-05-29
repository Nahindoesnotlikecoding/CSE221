import os, sys, time, random, threading, subprocess

# Compile and run: pypy _219_Testing.py
def solve(listA, listB):
    N = len(listA)
    M = len(listB)
    # Place your code here
    return ""


N = 0
listA, listB= [], []

res = False

# stdin
# 10 4
# 2 4 1 5 6 8 1 2 7 7
# 4 8 2 7
N = int(input())
M = int(input())
listA = list(map(int, input().split()))
listB = list(map(int, input().split()))

start = time.time()
res = solve(listA.copy(), listB.copy())
finish = time.time()
elapsed = finish - start

# # stdout
print(res)

print("Execution time for the targeted one test is " + f"{elapsed:.9f}" + "s", flush=True)
os._exit(0)

# # file input
# with open("TimeLimitExceeded.txt") as fin:
# with open("CustomTest.txt") as fin:
# with open("WrongAnswer.txt") as fin:
#     listA = list(map(int, fin.readlines()[3][8:-2].split(", ")))
#     listB = list(map(int, fin.readlines()[3][10:-2].split(", ")))

# # hardcoded input
# listA = [7, 4, 9, 3, 2, 5, 1]
# listB = [40, 50, 50, 20, 10, 10, 10]


# # file output
# with open("OutputOfYourCode.txt", "w") as fout:
#     fout.write(str(res))
