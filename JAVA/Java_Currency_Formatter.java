import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.text.NumberFormat; 
public class Java_Currency_Formatter {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double payment = scanner.nextDouble();
        scanner.close();
        
        NumberFormat formatter1=NumberFormat.getCurrencyInstance(Locale.US);  
        String us=formatter1.format(payment);
        NumberFormat formatter2=NumberFormat.getCurrencyInstance(new Locale("en", "in"));  
        String india=formatter2.format(payment);
        NumberFormat formatter3=NumberFormat.getCurrencyInstance(Locale.CHINA);  
        String china=formatter3.format(payment);
        NumberFormat formatter4=NumberFormat.getCurrencyInstance(Locale.FRANCE);  
        String france=formatter4.format(payment);
        
        
        // Write your code here.
        
        System.out.println("US: " + us);
        System.out.println("India: " + india);
        System.out.println("China: " + china);
        System.out.println("France: " + france);
    }
}
