import java.io.*;
import java.util.*;

// Compile and run: javac _219_Testing.java && java _219_Testing

class _219_Solution {
    public static String solve(ArrayList<Integer> listA,
            ArrayList<Integer> listB) {
        int N = listA.size(), M = listB.size();
        String res = "";
        // place your code here
        return res;
    }
}

public class _219_Testing {
    Random rng = new Random();
    public static int N = 0;
    public static int M = 0;
    public static ArrayList<Integer> listA = new ArrayList<>(), listB = new ArrayList<>();
    public static String res;

    public static void main(String args[]) throws Exception {
        // stdin
        // 10 4
        // 2 4 1 5 6 8 1 2 7 7
        // 4 8 2 7
        BufferedReader fin = new BufferedReader(new InputStreamReader(System.in));
        String[] input = fin.readLine().split(" ");
        N = Integer.parseInt(input[0]);
        M = Integer.parseInt(input[1]);
        for (String temp : fin.readLine().split(" "))
            listA.add(Integer.parseInt(temp));
        for (String temp : fin.readLine().split(" "))
            listB.add(Integer.parseInt(temp));

        long start = System.nanoTime();
        res = _219_Solution.solve(new ArrayList<>(listA), new ArrayList<>(listB));
        long finish = System.nanoTime();
        long elapsed = finish - start;

        // // stdout
        System.out.println(listA.toString());

        System.out.printf("Execution time for the targeted one test is %.9fs\n", elapsed * 1e-9);
        System.exit(0);

        // // file input
        // BufferedReader fin = new BufferedReader(new
        // FileReader("TimeLimitExceeded.txt"));
        // BufferedReader fin = new BufferedReader(new FileReader("CustomTest.txt"));
        // BufferedReader fin = new BufferedReader(new FileReader("WrongAnswer.txt"));
        // for (int i = 1; i <= 3; ++i)
        // fin.readLine();
        // fin.skip(8);
        // for (String temp : fin.readLine().replace("]", "").split(", "))
        // listA.add(Integer.parseInt(temp));
        // fin.skip(10);
        // for (String temp : fin.readLine().replace("]", "").split(", "))
        // listA.add(Integer.parseInt(temp));
        // fin.close();

        // // hardcoded input
        // listA = new ArrayList<>(Arrays.asList(7, 4, 9, 3, 2, 5, 1));
        // listB = new ArrayList<>(Arrays.asList(40, 50, 50, 20, 10, 10, 10));

        // // file output
        // BufferedWriter fout = new BufferedWriter(new
        // FileWriter("OutputOfYourCode.txt"));
        // fout.write(listA.toString());
        // fout.close();
    }
}
