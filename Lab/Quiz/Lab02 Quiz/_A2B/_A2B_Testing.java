import java.util.*;
import java.io.*;

// Compile and run: javac _A2B_Testing.java && java _A2B_Testing
class _A2B_Solution {
    public static ArrayList<Integer> solve(Integer N, ArrayList<Integer> A, Integer M, ArrayList<Integer> B) {
        ArrayList<Integer> res = new ArrayList<>();
        // Place your code here
        return res;
    }
}

public class _A2B_Testing {
    Random rng = new Random();
    public static Integer N = 0, M = 0;
    public static ArrayList<Integer> A = new ArrayList<>();
    public static ArrayList<Integer> B = new ArrayList<>();
    public static ArrayList<Integer> res = new ArrayList<>();

    public static void main(String args[]) throws Exception {
        // // stdin
        // // 4
        // // 1 3 5 7
        // // 4
        // // 2 2 4 8
        BufferedReader fin = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(fin.readLine());
        for (String temp : fin.readLine().split(" "))
            A.add(Integer.parseInt(temp));
        M = Integer.parseInt(fin.readLine());
        for (String temp : fin.readLine().split(" "))
            B.add(Integer.parseInt(temp));

        // // hardcoded input
        // N = 4
        // A = new ArrayList<Integer>({1, 3, 5, 7});
        // M = 4
        // B = new ArrayList<Integer>({2, 2, 4, 8});

        long start = System.nanoTime();
        res = _A2B_Solution.solve(N, new ArrayList<>(A), M, new ArrayList<>(B));
        long finish = System.nanoTime();
        long elapsed = finish - start;

        // stdout
        // System.out.println(res.toString());

        System.out.printf("Execution time for the targeted one test is %.9fs\n", elapsed * 1e-9);
        System.exit(0);

        // // file input
        // BufferedReader fin = new BufferedReader(new
        // FileReader("TimeLimitExceeded.txt"));
        // BufferedReader fin = new BufferedReader(new FileReader("CustomTest.txt"));
        // BufferedReader fin = new BufferedReader(new FileReader("WrongAnswer.txt"));
        // for (int i = 1; i <= 2; ++i)
        // fin.readLine();
        // N = Integer.parseInt(fin.readLine().split(" ")[2]);
        // String[] temp = fin.readLine().split(" ");
        // for(int i = 0; i < N; i++){
        // if(i == 0)
        // A.add(Integer.parseInt(temp[2].substring(1, temp[2].length() - 1)));
        // else
        // A.add(Integer.parseInt(temp[i + 2].substring(0, temp[i + 2].length() - 1)));
        // }
        // M = Integer.parseInt(fin.readLine().split(" ")[2]);
        // temp = fin.readLine().split(" ");
        // for(int i = 0; i < M; i++){
        // if(i == 0)
        // B.add(Integer.parseInt(temp[2].substring(1, temp[2].length() - 1)));
        // else
        // B.add(Integer.parseInt(temp[i + 2].substring(0, temp[i + 2].length() - 1)));
        // }
        // fin.close();

        // // file output
        // BufferedWriter fout = new BufferedWriter(new
        // FileWriter("OutputOfYourCode.txt"));
        // fout.write(res.toString());
        // fout.close();
    }
}
