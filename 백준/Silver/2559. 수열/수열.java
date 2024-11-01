import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();

        int[] items = new int[n];
        for (int i =0; i<n; i++){
            items[i] = sc.nextInt();
        }


        
        // 전체 - (짝-1) 번에서 멈춤 
        int renum = n-(k-1);
        int sum = 0;

        for (int i=0; i<k; i++){
            sum += items[i];
        }
        int answer = sum;

        for (int i=k; i<n; i++){
            sum += items[i] - items[i-k];
            answer = Math.max(answer,sum);
        }

        System.out.print(answer);
    }
}