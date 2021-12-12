import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> list = new ArrayList<>();

        for(int i=0;i<10;i++){
            int term = (sc.nextInt()%42);

            if(i!=0){
                if(!list.contains(term)){
                    list.add(term);
                }
            }
            else{
                list.add(term);
            }
        }
        System.out.println(list.size());
    }
}
