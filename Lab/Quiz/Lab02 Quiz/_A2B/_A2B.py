import os, sys, time, random, threading, subprocess
from _A2B_Solution import solve
test, best, score, batch, total = 0, 0, 0, 0, 0
timeLimit, nBatch = 1, 10
weight = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
nTest = [0, 10, 100, 100, 100, 100, 100, 100, 10, 10, 10]
maxN = [ 0, 10, 10, 100, 100, 1000, 1000, 10000, 100000, 1000000, 1000000]
maxA = [0, 1_000, 1_000_000, 1_000_000, 1_000_000_000, 1_000_000, 1_000_000_000, 1_000_000, 1_000_000_000, 1_000_000, 1_000_000_000]
N, M = 0, 0
A = []
B = []
res = None
def printCase(verdict, test, N, A, M, B):
    if os.path.getsize(verdict + ".txt") == 0:
        with open(verdict + ".txt", "w") as fout:
            fout.write("batch = " + str(batch) + "\ntest = " + str(test) + "\n")
            fout.write("N = " + str(N) + "\n")
            fout.write("A = " + str(A) + "\n")
            fout.write("M = " + str(M) + "\n")
            fout.write("B = " + str(B) + "\n")
    print(verdict + " on Batch " + str(batch), flush=True)
def exitCase(verdict):
    printCase(verdict, test, N, A, M, B)
    os._exit(1)
def checkSoln():
    if(res == None or len(res) != N + M):
        exitCase("WrongAnswer")
    i, j = 0, 0
    for x in res:
        if i < N and x == A[i]:
            i += 1
        elif j < M and x == B[j]:
            j += 1
        else:
            exitCase("WrongAnswer")
def processBatch():
    global test, N, A, M, B, res
    test = 1
    while test <= nTest[batch]:
        N = random.randint(2, maxN[batch])
        A = [None] * N
        D = maxA[batch] // N
        for i in range(N):
            A[i] = (random.randint(1 if i == 0 else A[i - 1], maxA[batch] - (N - i - 1) * D))
        M = random.randint(2, maxN[batch])
        B = [None] * M
        D = maxA[batch] // M
        for i in range(M):
            B[i] = (random.randint(1 if i == 0 else B[i - 1], maxA[batch] - (M - i - 1) * D))
        res = solve(N, A.copy(), M, B.copy())
        checkSoln()
        test += 1
        
def limitTime():
    time.sleep(timeLimit)
    exitCase("TimeLimitExceeded")
if len(sys.argv) == 2:
    batch = int(sys.argv[1])
    random.seed(batch)
if 1 <= batch and batch <= nBatch:
    print("Running on Batch " + str(batch), flush=True)
    start = time.time()
    threading.Thread(target=limitTime, daemon=True).start()
    processBatch()
    finish = time.time()
    elapsed = finish - start
    print("Passed Batch " + str(batch) + " in " + f"{elapsed:.9f}" + "s", flush=True)
    os._exit(0)
ID = ""
with open("EnterIDandLanguage.txt") as fin:
    ID = fin.readline().split()[0]
if os.path.exists("_A2B_" + ID + ".py"):
    with open("_A2B_" + ID + ".py") as fin:
        best = int(fin.readline().split()[2])
open("WrongAnswer.txt", "w").close()
open("TimeLimitExceeded.txt", "w").close()
batch = 1
while batch <= nBatch:
    process = subprocess.run("pypy _A2B.py " + str(batch), capture_output=True, text=True)
    if process.stdout:
        print(process.stdout, end="")
    if process.stderr:
        print(process.stderr, end="")
    if process.returncode == 0:
        score += weight[batch]
    total += weight[batch]
    batch += 1
if best <= score:
    with open("_A2B_" + ID + ".py", "w") as fout:
        fout.write("# " + ID + " " + str(score) + "\n")
    subprocess.run("cmd /c echo # %COMPUTERNAME% %USERNAME%>>_A2B_" + ID + ".py")
    with open("_A2B_" + ID + ".py", "a") as fout:
        with open("_A2B_Solution.py") as code:
            fout.write(code.read())
print("Tentative score = " + str(score / total) + "/1", flush=True)
os._exit(0)
