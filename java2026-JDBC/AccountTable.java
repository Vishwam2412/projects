import java.sql.Statement;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
// import java.util.*;

public class AccountTable{
    public static void main(String []args){
        String url = "jdbc:mariadb://127.0.0.1:3306/java2026";
        String usr = "root";
        String passwd = "java2026";

        try{
            Connection conn = DriverManager.getConnection(url,usr,passwd);
            Statement st = conn.createStatement();

            st.execute("USE java2026");

            st.execute("DROP TABLE accounts");
            
            String sqli = "CREATE TABLE accounts("+
                        "acc_no INT PRIMARY KEY,"+
                        "name VARCHAR(30),"+
                        "balance DOUBLE)";

            String fv = "INSERT IGNORE INTO accounts VALUES (123,'sagar',23878.12)";
            String sv = "INSERT IGNORE INTO accounts VALUES (129,'mob',1221.878)";
            String tv = "INSERT IGNORE INTO accounts VALUES (334,'kin',23837.12)";
            st.execute(sqli);
            st.execute(fv);
            st.execute(sv);
            st.execute(tv);
            
            System.out.println("-----BALANCE-----");
            ResultSet rst = st.executeQuery("SELECT * FROM accounts");
            
            while(rst.next()){
                int id = rst.getInt("acc_no");
                String name = rst.getString("name");
                Double bal = rst.getDouble("balance");
                System.out.println("ID: "+id+" | Name: "+name+" | Balance: "+bal);
            }
            rst.close();
            try{
                
                conn.setAutoCommit(false);
                
                st.execute("UPDATE accounts SET balance = balance-1000 WHERE acc_no=334");
                st.execute("UPDATE accounts SET balance = balance+1000 WHERE acc_no=129");
                
                conn.commit();
                System.out.println("Balance Added Successfully");
                
                System.out.println("-----UPDATED-BALANCE-----");
                ResultSet arv = st.executeQuery("SELECT * FROM accounts");
                
                while(arv.next()){
                    int id = arv.getInt("acc_no");
                    String name = arv.getString("name");
                    Double bal = arv.getDouble("balance");
                    System.out.println("ID: "+id+" | Name: "+name+" | Balance: "+bal);
                }

                arv.close();

            }catch(Exception e){
                conn.rollback(); 
                System.out.println("Transaction failed. Rolling back changes.");
                e.printStackTrace();
            }

            conn.close();

        }catch(Exception e){
            e.printStackTrace();
        }
    }
}