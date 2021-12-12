import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int B = A;
        int count=0;

        while(true){
            B = (B%10)*10  + (((B/10)+(B%10))%10);
            count++;

            if(B==A){
                System.out.println(count);
                break;
            }
        }
    }
}