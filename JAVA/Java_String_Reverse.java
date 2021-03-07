import java.io.*;
import java.util.*;

public class Java_String_Reverse

 {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String str="";
        for(int i=A.length()-1;i>=0;i--)
        {
            str+=A.charAt(i);
        }
        if(A.equals(str))
        {
            System.out.println("Yes");
        }
        else
        {
            System.out.println("No");
        }
        /* Enter your code here. Print output to STDOUT. */
        
    }
}



