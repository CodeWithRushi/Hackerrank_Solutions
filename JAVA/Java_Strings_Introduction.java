import java.io.*;
import java.util.*;

public class Java_Strings_Introduction

 {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String B=sc.next();
        int c=A.length()+B.length();
        System.out.println(c);
        if(A.charAt(0)>B.charAt(0))
        {
            System.out.println("Yes");
        }
        else
        {
            System.out.println("No");
        }
         String First=A.substring(0,1).toUpperCase()+A.substring(1);
         String Second=B.substring(0,1).toUpperCase()+B.substring(1);
         System.out.println(First+" "+Second);
        /* Enter your code here. Print output to STDOUT. */
        
    }
}



