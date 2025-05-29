#include<bits/extc++.h>
using namespace std;
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

// Compile and run: c++ _219_Testing.cpp && .\a.exe
string solve(vector<int> listA, vector<int> listB) {
    int N = listA.size(), M = listB.size();
    bool isSubsequence = false;
    // Place your code here

    if (isSubsequence == true) {
        return "Yes";
    }
    else {
        return "No";
    }
}
int N = 0, M = 0;
vector<int> listA, listB;
string res;
int main() {
    // stdin
    // 10 4
    // 2 4 1 5 6 8 1 2 7 7
    // 4 8 2 7
    cin >> N;
    cin >> M;
    for (int i = 1, j; i <= N; ++i)
        cin >> j, listA.push_back(j);
    for (int i = 1, j; i <= N; ++i)
        cin >> j, listB.push_back(j);


    chrono::_V2::system_clock::time_point start = chrono::high_resolution_clock::now();
    res = solve(listA, listB);
    chrono::_V2::system_clock::time_point finish = chrono::high_resolution_clock::now();
    chrono::_V2::system_clock::duration elapsed = chrono::duration_cast<chrono::nanoseconds>(finish - start);

    // // stdout
    cout << res << "\n";

    cout << fixed << setprecision(9) << "Execution time for the targeted one test is " << (elapsed.count() * 1e-9) << "s\n";
    exit(0);

    // // file input
    // ifstream fin("TimeLimitExceeded.txt");
    // ifstream fin("CustomTest.txt");
    // ifstream fin("WrongAnswer.txt");
    // string temp;
    // for (int i = 1; i <= 3; ++i) getline(fin, temp);
    // fin.ignore(8), getline(fin, temp);
    // for (istringstream sin(temp); sin >> temp; sIDs.push_back(stoi(temp)))
    //     temp.pop_back();
    // fin.ignore(10), getline(fin, temp);
    // for (istringstream sin(temp); sin >> temp; sMarks.push_back(stoi(temp)))
    //     temp.pop_back();
    // fin.close();


    // // hardcoded input
    // sIDs = vector<int>({ 7, 4, 9, 3, 2, 5, 1 });
    // sMarks = vector<int>({ 40, 50, 50, 20, 10, 10, 10 });


    // // file output
    // ofstream fout("OutputOfYourCode.txt");
    // fout << to_string(res);
    // fout.close();
}
