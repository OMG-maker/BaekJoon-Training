import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        double[] arr = new double[A];
        double max = sc.nextInt();
        double sum = 0.0;
        arr[0] = max;

        for(int i=1;i<A;i++){
            arr[i] = sc.nextInt();
            if (arr[i]>max){
                max = arr[i];
            }
        }

        for(int i=0;i<A;i++){
            sum += (arr[i]/max)*100.0;
        }

        System.out.println(sum/A);
    }
}