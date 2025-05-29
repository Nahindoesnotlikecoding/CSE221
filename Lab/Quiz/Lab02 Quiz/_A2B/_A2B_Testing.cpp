#include<bits/stdc++.h>
using namespace std;
extern pair<int, vector<pair<int, int>>> solve(vector<int> sIDs, vector<int> sMarks);
inline int rng(int x) { return abs(rand() << 30LL | rand() << 15LL | rand()) % x; }
inline string to_string(vector<int>& x) {
    string y = "[";
    if (!x.empty()) y += to_string(x[0]);
    for (int i = 1; i < x.size(); ++i)
        y += ", " + to_string(x[i]);
    return y + "]";
}
inline string to_string(pair<int, int>& x) {
    return "(" + to_string(x.first) + ", " + to_string(x.second) + ")";
}
inline string to_string(vector<pair<int, int>>& x) {
    string y = "[";
    if (!x.empty()) y += to_string(x[0]);
    for (int i = 1; i < x.size(); ++i)
        y += ", " + to_string(x[i]);
    return y + "]";
}
inline string to_string(pair<int, vector<pair<int, int>>>& x) {
    return "(" + to_string(x.first) + ", " + to_string(x.second) + ")";
}
int N, M;
vector<int> A, B;
vector<int> res;
// Compile and run: c++ _A2B_Testing.cpp && .\a.exe
vector<int> solve(int N, vector<int> A, int M, vector<int> B) {
    vector<int> res;
    // Place your code here
    return res;
}


int main() {

    // // stdin
    // // 4
    // // 1 3 5 7
    // // 4
    // // 2 2 4 8
    cin >> N;
    for (int i = 1, j; i <= N; ++i)
        cin >> j, A.push_back(j);
    cin >> M;
    for (int i = 1, j; i <= M; ++i)
        cin >> j, B.push_back(j);

    // // hardcoded input
    // N = 4;
    // A = {1, 3, 5, 7};
    // M = 4;
    // B = {2 2 4 8};

    chrono::_V2::system_clock::time_point start = chrono::high_resolution_clock::now();
    res = solve(N, A, M, B);
    chrono::_V2::system_clock::time_point finish = chrono::high_resolution_clock::now();
    chrono::_V2::system_clock::duration elapsed = chrono::duration_cast<chrono::nanoseconds>(finish - start);


    // stdout
    // cout << to_string(res) << "\n";

    cout << fixed << setprecision(9) << "Execution time for the targeted one test is " << (elapsed.count() * 1e-9) << "s\n";
    exit(0);


    // // file input
    // ifstream fin("TimeLimitExceeded.txt");
    // ifstream fin("CustomTest.txt");
    // ifstream fin("WrongAnswer.txt");
    // string temp;
    // for (int i = 1; i <= 2; ++i) getline(fin, temp);
    // fin >> temp >> temp >> N;
    // fin >> temp >> temp;
    // char t;
    // for (int i = 0, j; i < N; i++)
    //     fin >> t >> j, A.push_back(j);
    // fin >> t >> temp >> temp >> M;
    // fin >> temp >> temp;
    // for (int i = 0, j; i < M; i++)
    //     fin >> t >> j, B.push_back(j);
    // fin.close();


    // // file output
    // ofstream fout("OutputOfYourCode.txt");
    // fout << to_string(res);
    // fout.close();
}
