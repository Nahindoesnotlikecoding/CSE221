#include<bits/extc++.h>
using namespace std;
mt19937 rng;
/*#define dbg(a) cout << "->" << __LINE__ << ": " << #a << " = " << a << endl
inline void printList(vector<int> &v)
{
    for(int x :v)
    {
        printf("%d ",x);
    }
    printf("\n");
}*/
inline int randInt(int x, int y) { return uniform_int_distribution<int>(x, y)(rng); }
inline string to_string(vector<int>& x) {
    string y = "[";
    if (!x.empty()) y += to_string(x[0]);
    for (int i = 1; i < x.size(); ++i)
        y += ", " + to_string(x[i]);
    return y + "]";
}
const int MAGIC = 7;
int test = 0, best = 0, score = 0, batch = 0, total = 0;
int timeLimit = 1, nBatch = 10, N = 0, M = 0;
int weight[] = { 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 };
int nTest[] = { 0, 10, 1000, 100000, 10, 100, 1000, 10000, 1, 10, 100 };
int maxN[] = { 0, 10, 10, 10, 100, 100, 100, 100, 1000, 1000, 1000 };
vector<int> listA, listB;
string res;
map<int, string> verd;
extern string solve(vector<int> listA, vector<int> listB);
inline void printCase(string& verdict, int test, vector<int> listA, vector<int> listB) {
    if (ifstream(verdict + ".txt").peek() == ifstream::traits_type::eof()) {
        ofstream fout(verdict + ".txt");
        fout << "batch = " << to_string(batch) << "\ntest = " << to_string(test) << "\n";
        fout << "N = " << to_string(listA.size()) << "\n";
        fout << "M = " << to_string(listB.size()) << "\n";
        fout << "listA = " << to_string(listA) << "\n";
        fout << "listB = " << to_string(listB) << "\n";
    }
    cout << verdict << " on Batch " << batch << "\n";
}
inline void exitCase(string verdict) {
    printCase(verdict, test, listA, listB), exit(1);
}
inline void checkSoln(int way) {
    if(res!=verd[way]) {
        exitCase("WrongAnswer");
    } 
}
inline void generateSequences(int way) {

    for(int i = 1; i<=N; i++)
    {
        listA.push_back(randInt(-1000000, 1000000));
    }

    int sz = 0;
    for(int i = 0; i<N and sz < M; i++)
    {
        int rem = M - sz;
        int take = randInt(0,1);
        if(take or rem == (N-i)) 
        {
            listB.push_back(listA[i]);
            sz++;
        }
    }
    
    if(!way)
    {
        int cng = randInt(0,M-1);
        if(listB[cng]==0)
        {
            listB[cng] += MAGIC;
        }
        else
        {
            listB[cng] *= -1;
        }
    }
    return;
}

inline void processBatch() {
    
    for (test = 1; test <= nTest[batch]; ++test) {
        int way = randInt(0,1);
        listA.clear(), listB.clear();
        N = randInt(1, maxN[batch]);
        M = randInt(1, N);
        listA.reserve(N), listB.reserve(M);
        generateSequences(way);
        res = solve(listA, listB), checkSoln(way);
    }
}
inline void limitTime() {
    this_thread::sleep_for(chrono::seconds(timeLimit));
    exitCase("TimeLimitExceeded");
}
int main(int argc, char** argv) {
    verd[0] = "No";
    verd[1] = "Yes";
    if (argc == 2) rng.seed(batch = stoi(argv[1]));
    if (1 <= batch && batch <= nBatch) {
        cout << "Running on Batch " << batch << endl;
        chrono::_V2::system_clock::time_point start = chrono::high_resolution_clock::now();
        thread(limitTime).detach(), processBatch();
        chrono::_V2::system_clock::time_point finish = chrono::high_resolution_clock::now();
        chrono::_V2::system_clock::duration elapsed = chrono::duration_cast<chrono::nanoseconds>(finish - start);
        cout << fixed << setprecision(9) << "Passed Batch " << batch << " in " << (elapsed.count() * 1e-9) << "s\n", exit(0);
    }
    string ID;
    ifstream("EnterIDandLanguage.txt") >> ID;
    if (ifstream("_219_" + ID + ".cpp"))
        ifstream("_219_" + ID + ".cpp").ignore(12) >> best;
    ofstream("WrongAnswer.txt").close();
    ofstream("TimeLimitExceeded.txt").close();
    for (batch = 1; batch <= nBatch; total += weight[batch], ++batch)
        if (!system((".\\a.exe " + to_string(batch)).c_str()))
            score += weight[batch];
    if (best <= score) {
        ofstream("_219_" + ID + ".cpp") << "// " << ID << " " << score << "\n";
        system(("echo // %COMPUTERNAME% %USERNAME%>>_219_" + ID + ".cpp").c_str());
        ifstream fin("_219_Solution.cpp");
        ofstream("_219_" + ID + ".cpp", ios::app) << string("").assign(istreambuf_iterator<char>(fin), std::istreambuf_iterator<char>());
    }
    cout << "Tentative score = " << double(score) / total << "/1\n", exit(0);
}
