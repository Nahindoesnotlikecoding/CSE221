import os, sys, time, random, threading, subprocess
from _219_Solution import solve
MAGIC = 7
test, best, score, batch, total = 0, 0, 0, 0, 0
timeLimit, nBatch, N, M = 1, 10, 0, 0
weight = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
nTest = [0, 10, 1000, 100000, 10, 100, 1000, 10000, 1, 10, 100]
maxN = [0, 10, 10, 10, 100, 100, 100, 100, 1000, 1000, 1000]
listA, listB = [], []
res = None
verd = {}
def printCase(verdict, test, listA, listB):
    if os.path.getsize(verdict + ".txt") == 0:
        with open(verdict + ".txt", "w") as fout:
            fout.write("batch = " + str(batch) + "\ntest = " + str(test) + "\n")
            fout.write("N = " + str(len(listA)) + "\n")
            fout.write("M = " + str(len(listB)) + "\n")
            fout.write("listA = " + str(listA) + "\n")
            fout.write("listB = " + str(listB) + "\n")
    print(verdict + " on Batch " + str(batch), flush=True)
def exitCase(verdict):
    printCase(verdict, test, listA.copy(), listB.copy())
    os._exit(1)
def checkSoln(way):
    if res!=verd[way]:
        exitCase("WrongAnswer")
def generateSequences(way):
    for i in range(N):
        listA.append(random.randint(-100000,100000))
    sz = 0
    for i in range(N):
        rem = M - sz
        take = random.randint(0,1)
        if take == 1 or rem == N-i:
            listB.append(listA[i])
            sz = sz + 1
            if sz == M:
                break
    
    if way%2==0:
        cng = random.randint(0,M-1)
        if listB[cng]==0:
            listB[cng] += MAGIC
        else:
            listB[cng] *= -1
       
    
def processBatch():
    global test, N, M, listA, listB, res
    test = 1
    while test <= nTest[batch]:
        listA = []
        listB = []
        N = random.randint(1, maxN[batch])
        M = random.randint(1, N)
        way = random.randint(0, 1)
        generateSequences(way)
        res = solve(listA.copy(), listB.copy())
        checkSoln(way)
        test += 1
        
def limitTime():
    time.sleep(timeLimit)
    exitCase("TimeLimitExceeded")
verd[0] = "No"
verd[1] = "Yes"
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
if os.path.exists("_219_" + ID + ".py"):
    with open("_219_" + ID + ".py") as fin:
        best = int(fin.readline().split()[2])
open("WrongAnswer.txt", "w").close()
open("TimeLimitExceeded.txt", "w").close()
batch = 1
while batch <= nBatch:
    process = subprocess.run("pypy _219.py " + str(batch), capture_output=True, text=True)
    if process.stdout:
        print(process.stdout, end="")
    if process.stderr:
        print(process.stderr, end="")
    if process.returncode == 0:
        score += weight[batch]
    total += weight[batch]
    batch += 1
if best <= score:
    with open("_219_" + ID + ".py", "w") as fout:
        fout.write("# " + ID + " " + str(score) + "\n")
    subprocess.run("cmd /c echo # %COMPUTERNAME% %USERNAME%>>_219_" + ID + ".py")
    with open("_219_" + ID + ".py", "a") as fout:
        with open("_219_Solution.py") as code:
            fout.write(code.read())
print("Tentative score = " + str(score / total) + "/1", flush=True)
os._exit(0)
