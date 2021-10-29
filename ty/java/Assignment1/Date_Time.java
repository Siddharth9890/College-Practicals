import java.util.Date;
import java.text.SimpleDateFormat;

public class Date_Time {
    public static void main(String[] args) {  
        Date date = new Date();  
        SimpleDateFormat formatter = new SimpleDateFormat("MM/dd/yyyy");  
        String strDate = formatter.format(date);  
        System.out.println("Current date is: "+strDate); 
        
        formatter = new SimpleDateFormat("dd-MM-yyyy");  
        strDate = formatter.format(date);  
        System.out.println("Current date is  : "+strDate);
      
        formatter = new SimpleDateFormat("EEEE MMMM dd yyyy");  
        strDate = formatter.format(date);  
        System.out.println("Current date is  :"+strDate);  
      
        formatter = new SimpleDateFormat("EE MMMM dd HH:mm:ss z yyyy");  
        strDate = formatter.format(date);  
        System.out.println("Current date and time is  : "+strDate); 
        
        formatter = new SimpleDateFormat("MM/dd/yyyy hh:mm:ss  zzz");  
        strDate = formatter.format(date);  
        System.out.println("Current date and time is  : "+strDate);
      
        formatter = new SimpleDateFormat("HH:mm:ss");  
        strDate = formatter.format(date);  
        System.out.println("Current time is  : "+strDate);  
      
        formatter = new SimpleDateFormat("w");  
        strDate = formatter.format(date);  
        System.out.println("Current weak of year is : "+strDate);  

        formatter = new SimpleDateFormat("W");  
        strDate = formatter.format(date);  
        System.out.println("Current weak of month is : "+strDate);

        formatter = new SimpleDateFormat("D");  
        strDate = formatter.format(date);  
        System.out.println("Current day of year is : "+strDate);
    }  
}
