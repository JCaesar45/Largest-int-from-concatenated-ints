import java.util.*;

public class MaxCombine {
    public static long maxCombine(int[] xs) {
        if (xs == null || xs.length == 0) return 0L;
        List<String> nums = new ArrayList<>();
        for (int x : xs) {
            if (x >= 0) nums.add(String.valueOf(x));
        }
        if (nums.isEmpty()) return 0L;
        nums.sort((a, b) -> (b + a).compareTo(a + b));
        String joined = String.join("", nums);
        return joined.charAt(0) == '0' ? 0L : Long.parseLong(joined);
    }

    public static void main(String[] args) {
        int[][] inputs = {
            {1, 3, 3, 4, 55},
            {71, 45, 23, 4, 5},
            {14, 43, 53, 114, 55},
            {1, 34, 3, 98, 9, 76, 45, 4},
            {54, 546, 548, 60}
        };
        long[] expected = {554331L, 71545423L, 55534314114L, 998764543431L, 6054854654L};

        for (int i = 0; i < inputs.length; i++) {
            long result = maxCombine(inputs[i]);
            String status = result == expected[i] ? "PASS" : "FAIL";
            System.out.println(status + ": " + Arrays.toString(inputs[i]) + " -> " + result + " (expected " + expected[i] + ")");
        }
    }
}
