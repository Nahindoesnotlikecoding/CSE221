import java.util.*;
import java.io.*;

public class _A2B {
    public static Random rng = new Random();
    public static int test = 0, best = 0, score = 0, batch = 0, total = 0;
    public static int timeLimit = 1, nBatch = 10;
    public static int weight[] = { 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 };
    public static int nTest[] = { 0, 10, 100, 100, 100, 100, 100, 100, 10, 10, 10 };
    public static int maxN[] = { 0, 10, 10, 100, 100, 1000, 1000, 10000, 100000, 1000000, 1000000 };
    public static int maxA[] = { 0, 1_000, 1_000_000, 1_000_000, 1_000_000_000, 1_000_000, 1_000_000_000, 1_000_000,
            1_000_000_000, 1_000_000, 1_000_000_000 };
    public static ArrayList<Integer> A = new ArrayList<>();
    public static Integer N = 0;
    public static ArrayList<Integer> B = new ArrayList<>();
    public static Integer M = 0;

    public static ArrayList<Integer> res;

    public static void printCase(String verdict, int test, Integer N, ArrayList<Integer> A, Integer M,
            ArrayList<Integer> B)
            throws Exception {
        if (new File(verdict + ".txt").length() == 0) {
            BufferedWriter fout = new BufferedWriter(new FileWriter(verdict + ".txt"));
            fout.write("batch = " + batch + "\ntest = " + test + "\n");
            fout.write("N = " + N + "\n");
            fout.write("A = " + A + "\n");
            fout.write("M = " + M + "\n");
            fout.write("B = " + B + "\n");
            fout.close();
        }
        System.out.print(verdict + " on Batch " + batch + "\n");
    }

    public static void exitCase(String verdict) throws Exception {
        printCase(verdict, test, N, A, M, B);
        System.exit(1);
    }

    public static void checkSoln() throws Exception {
        if (res == null || res.size() != N + M)
            exitCase("WrongAnswer");
        int i = 0, j = 0;
        for (int x : res) {
            if (i < N && x == A.get(i))
                ++i;
            else if (j < M && x == B.get(j))
                ++j;
            else
                exitCase("WrongAnswer");
        }
    }

    public static void processBatch() throws Exception {
        for (test = 1; test <= nTest[batch]; ++test) {
            N = 2 + rng.nextInt(maxN[batch] - 1);
            A.clear();
            int D = maxA[batch] / N;
            for (int i = 0; i < N; ++i)
                A.add((i == 0 ? 1 : A.get(i - 1))
                        + rng.nextInt(maxA[batch] - (N - i - 1) * D + 1 - (i == 0 ? 1 : A.get(i - 1))));
            M = 2 + rng.nextInt(maxN[batch] - 1);
            B.clear();
            D = maxA[batch] / M;
            for (int i = 0; i < M; ++i)
                B.add((i == 0 ? 1 : B.get(i - 1))
                        + rng.nextInt(maxA[batch] - (M - i - 1) * D + 1 - (i == 0 ? 1 : B.get(i - 1))));
            res = _A2B_Solution.solve(N, new ArrayList<>(A), M, new ArrayList<>(B));
            checkSoln();
        }
    }

    public static void limitTime() {
        try {
            Thread.sleep(1000 * timeLimit);
            exitCase("TimeLimitExceeded");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void main(String args[]) throws Exception {
        if (args.length == 1)
            rng.setSeed(batch = Integer.parseInt(args[0]));
        if (1 <= batch && batch <= nBatch) {
            System.out.println("Running on Batch " + batch);
            long start = System.nanoTime();
            new Thread(() -> limitTime()).start();
            processBatch();
            long finish = System.nanoTime();
            long elapsed = finish - start;
            System.out.printf("Passed Batch " + batch + " in %.9fs\n", elapsed * 1e-9);
            System.exit(0);
        }
        BufferedReader fin = new BufferedReader(new FileReader("EnterIDandLanguage.txt"));
        String ID = fin.readLine().split("\\s+", 2)[0];
        fin.close();
        if (new File("_A2B_" + ID + ".java").exists()) {
            fin = new BufferedReader(new FileReader("_A2B_" + ID + ".java"));
            best = Integer.parseInt(fin.readLine().split("\\s+", 4)[2]);
            fin.close();
        }
        new FileOutputStream("WrongAnswer.txt").close();
        new FileOutputStream("TimeLimitExceeded.txt").close();
        for (batch = 1; batch <= nBatch; total += weight[batch], ++batch) {
            Process process = new ProcessBuilder("java", "_A2B", "" + batch).start();
            fin = new BufferedReader(new InputStreamReader(process.getInputStream()));
            fin.lines().forEach(System.out::println);
            fin.close();
            fin = new BufferedReader(new InputStreamReader(process.getErrorStream()));
            fin.lines().forEach(System.out::println);
            fin.close();
            if (process.waitFor() == 0)
                score += weight[batch];
        }
        if (best <= score) {
            BufferedWriter fout = new BufferedWriter(new FileWriter("_A2B_" + ID + ".java"));
            fout.write("// " + ID + " " + score + "\n");
            fout.close();
            new ProcessBuilder("cmd", "/c", "echo // %COMPUTERNAME% %USERNAME%>>_A2B_" + ID + ".java").start()
                    .waitFor();
            fout = new BufferedWriter(new FileWriter("_A2B_" + ID + ".java", true));
            fin = new BufferedReader(new FileReader("_A2B_Solution.java"));
            fout.write(fin.lines().collect(java.util.stream.Collectors.joining(System.lineSeparator())));
            fin.close();
            fout.close();
        }
        System.out.print("Tentative score = " + (score / (double) total) + "/1\n");
        System.exit(0);
    }
}
