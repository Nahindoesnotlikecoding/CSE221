import java.util.*;
import java.io.*;
import java.util.Map;
import java.util.HashMap;
public class _219 {
    public static Random rng = new Random();
    public static int test = 0, best = 0, score = 0, batch = 0, total = 0;
    public static int timeLimit = 1, nBatch = 10, N = 0, M = 0;
    public static int weight[] = { 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 };
    public static int nTest[] = { 0, 10, 1000, 100000, 10, 100, 1000, 10000, 1, 10, 100 };
    public static int maxN[] = { 0, 10, 10, 10, 100, 100, 100, 100, 1000, 1000, 1000 };
    public static ArrayList<Integer> listA = new ArrayList<>(), listB = new ArrayList<>();
    public static String res;
    public static Map<Integer, String> verd = new HashMap<>();
    final static int MAGIC = 7;

    public static void printCase(String verdict, int test, ArrayList<Integer> listA, ArrayList<Integer> listB)
            throws Exception {
        if (new File(verdict + ".txt").length() == 0) {
            BufferedWriter fout = new BufferedWriter(new FileWriter(verdict + ".txt"));
            fout.write("batch = " + batch + "\ntest = " + test + "\n");
            fout.write("N = " + listA.size() + "\n");
            fout.write("M = " + listA.size() + "\n");
            fout.write("listA = " + listA + "\n");
            fout.write("listB = " + listB + "\n");
            fout.close();
        }
        System.out.print(verdict + " on Batch " + batch + "\n");
    }

    public static void exitCase(String verdict) throws Exception {
        printCase(verdict, test, new ArrayList<>(listA), new ArrayList<>(listB));
        System.exit(1);
    }

    public static void checkSoln(int way) throws Exception {
        if(res!=verd.get(way))
            exitCase("WrongAnswer");
    }

    public static void generateSequences(int way) throws Exception {
        for(int i = 1; i<=N; i++)
        {
            listA.add(rng.nextInt(200001)-100000);
        }
        int sz = 0;
        for(int i = 0; i<N; i++)
        {
            int rem = M - sz;
            int take = rng.nextInt(2);
            if((take == 1) || (rem == N - i))
            {
                listB.add(listA.get(i));
                sz = sz + 1;
                if(sz==M)
                {
                    break;
                }
            }
            
        }
        if(way%2==0)
        {
            int cng = rng.nextInt(M);
            if(listB.get(cng)==0)
            {
                listB.set(cng, MAGIC);
            }
            else
            {
                listB.set(cng, -listB.get(cng));
            }
        }
    }

    public static void processBatch() throws Exception {
        for (test = 1; test <= nTest[batch]; ++test) {
            listA.clear();
            listB.clear();
            N = 1 + rng.nextInt(maxN[batch]);
            M = 1 + rng.nextInt(N);
            int way = rng.nextInt(2);
            generateSequences(way);
            res = _219_Solution.solve(new ArrayList<>(listA), new ArrayList<>(listB));
            checkSoln(way);
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
        verd.put(0, "No");
        verd.put(1, "Yes");
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
        if (new File("_219_" + ID + ".java").exists()) {
            fin = new BufferedReader(new FileReader("_219_" + ID + ".java"));
            best = Integer.parseInt(fin.readLine().split("\\s+", 4)[2]);
            fin.close();
        }
        new FileOutputStream("WrongAnswer.txt").close();
        new FileOutputStream("TimeLimitExceeded.txt").close();
        for (batch = 1; batch <= nBatch; total += weight[batch], ++batch) {
            Process process = new ProcessBuilder("java", "_219", "" + batch).start();
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
            BufferedWriter fout = new BufferedWriter(new FileWriter("_219_" + ID + ".java"));
            fout.write("// " + ID + " " + score + "\n");
            fout.close();
            new ProcessBuilder("cmd", "/c", "echo // %COMPUTERNAME% %USERNAME%>>_219_" + ID + ".java").start()
                    .waitFor();
            fout = new BufferedWriter(new FileWriter("_219_" + ID + ".java", true));
            fin = new BufferedReader(new FileReader("_219_Solution.java"));
            fout.write(fin.lines().collect(java.util.stream.Collectors.joining(System.lineSeparator())));
            fin.close();
            fout.close();
        }
        System.out.print("Tentative score = " + (score / (double) total) + "/1\n");
        System.exit(0);
    }
}
