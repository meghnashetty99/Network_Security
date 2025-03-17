import java.util.Scanner;
public class DESKeyGeneration {
private static final int[] PC1 = {
57, 49, 41, 33, 25, 17, 9,
1, 58, 50, 42, 34, 26, 18,
10, 2, 59, 51, 43, 35, 27,
19, 11, 3, 60, 52, 44, 36,
63, 55, 47, 39, 31, 23, 15,
7, 62, 54, 46, 38, 30, 22,
14, 6, 61, 53, 45, 37, 29,
21, 13, 5, 28, 20, 12, 4
};
private static final int[] PC2 = {
14, 17, 11, 24, 1, 5,
3, 28, 15, 6, 21, 10,
23, 19, 12, 4, 26, 8,
16, 7, 27, 20, 13, 2,
41, 52, 31, 37, 47, 55,
30, 40, 51, 45, 33, 48,
44, 49, 39, 56, 34, 53,
46, 42, 50, 36, 29, 32
};
private static final int[] SHIFTS = {1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1};
private static String permute(String input, int[] table) {
StringBuilder output = new StringBuilder();
for (int index : table) {
output.append(input.charAt(index - 1));
}
return output.toString();
}
private static String leftShift(String input, int shifts) {
return input.substring(shifts) + input.substring(0, shifts);
}
public static void main(String[] args) {
Scanner scanner = new Scanner(System.in);
System.out.println("Enter 64-bit key (binary): ");
String key = scanner.nextLine();
String permutedKey = permute(key, PC1);
String c = permutedKey.substring(0, 28);
String d = permutedKey.substring(28);
System.out.println("Generated Subkeys:");
for (int i = 0; i < 16; i++) {
c = leftShift(c, SHIFTS[i]);
d = leftShift(d, SHIFTS[i]);
String combined = c + d;
String subkey = permute(combined, PC2);System.out.println("Subkey " + (i + 1) + ": " + subkey);
}
scanner.close();}
}
