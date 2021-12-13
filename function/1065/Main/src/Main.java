import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int count=0;

        for (int i=1;i<=A;i++){
            String s = String.valueOf(i);

            if(s.length()<=2){
                count++;
            }
            else{
                int term;
                term = (s.charAt(0)- '0')- (s.charAt(1)- '0');
                int y_n=0;

                for(int j=1;j<s.length()-1;j++){
                    int term2 = (s.charAt(j)- '0')- (s.charAt(j+1)- '0');
                    if(term != term2){
                        y_n++;
                        break;
                    }
                }
                if(y_n==0){
                    count++;
                }
            }
        }
        System.out.println(count);
    }
}