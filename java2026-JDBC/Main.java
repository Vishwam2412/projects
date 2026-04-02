import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;
import java.sql.ResultSet;
import java.util.Scanner;


public class Main{
    public static void main(String []args){
       String url = "jdbc:mariadb://127.0.0.1:3306/java2026";
       String usr = "root";
       String pass = "java2026";

       try{
            Connection conn = DriverManager.getConnection(url,usr,pass);
            Statement st = conn.createStatement();
            st.execute("USE java2026");
            st.execute("DROP TABLE IF EXISTS students");
            st.execute("CREATE TABLE students"+
                        "(id INT PRIMARY KEY AUTO_INCREMENT,"+
                        "name VARCHAR(50),"+
                        "age INT,"+
                        "grade VARCHAR(1))"
            );

            Scanner sc = new Scanner(System.in); 
            System.out.printf("Enter the Number of Students : ");
            int nt = sc.nextInt();
            sc.nextLine();
            for(int i = 0 ; i<nt ; ++i){
                System.out.println("Enter student : Name Age Grade");
               String name = sc.nextLine();
               int age = sc.nextInt();
               char grade = sc.next().charAt(0);
               String sql = "INSERT INTO students (name ,age, grade) VALUES ('"+name+"'),('"+age+"'),('"+grade+"')";
               st.execute(sql);
               sc.nextLine();
            }
            ResultSet rst = st.executeQuery("USE java2026");
       }catch(Exception e){
        e.printStackTrace();
       }
    }
}