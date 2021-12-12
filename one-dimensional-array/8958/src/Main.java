import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        String[] sArr = new String[A];

        int sum = 0;
        int semiSum = 0;

        for (int i=0;i<A;i++){
            sArr[i] = sc.next();
        }

        for (int i=0;i<A;i++){
            for (int j=0;j<sArr[i].length();j++){
                if (sArr[i].charAt(j)=='O'){
                    semiSum++;
                    sum += semiSum;
                }
                else{
                    semiSum = 0;
                }
            }
            System.out.println(sum);
            semiSum=0;
            sum=0;
        }


    }
}