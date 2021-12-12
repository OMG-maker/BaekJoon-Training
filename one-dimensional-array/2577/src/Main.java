import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();

        String result = String.valueOf(A*B*C);

        for(int i=0;i<10;i++){
            System.out.println(countChar(result, i));
        }

    }
    public static int countChar(String str, int ch) {
        int count = 0;
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == (Integer.toString(ch)).charAt(0)) {
                count++;
            }
        }
        return count;
    }
}