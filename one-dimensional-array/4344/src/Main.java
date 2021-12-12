import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();

        for (int i=0;i<A;i++){
            int term = sc.nextInt();
            int sum = 0;
            int[] scoreArr = new int[term];

            for (int j=0;j<term;j++){
                scoreArr[j] = sc.nextInt();
                sum += scoreArr[j];
            }
            double scoreArrTerm = (double)sum/term;

            int count = 0;

            for (int j=0;j<term;j++){
                if (scoreArr[j]>scoreArrTerm){
                    count ++;
                }
            }
            System.out.println(String.format("%.3f", (double)count*100/term) +"%");
        }
    }
}