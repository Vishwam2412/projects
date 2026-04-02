import java.sql.DriverManager;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;

public class App{
    public static void main(String[]args){
        String url = "jdbc:mariadb://127.0.0.1:3306/java2026";
        String usr = "root";
        String passwd = "java2026";
        try{
            Connection conn = DriverManager.getConnection(url,usr,passwd);
            Statement st = conn.createStatement();
            // ResultSet rs = st.executeQuery("USE java2026;");
            String sql = "CREATE TABLE IF NOT EXISTS emp(name VARCHAR(24),city VARCHAR(24))";

            st.execute("TRUNCATE TABLE emp");
            st.execute("USE java2026");
            st.execute(sql);
            st.execute("INSERT IGNORE INTO emp(name,city) VALUES ('rahul','Bihar'),('Pankaj','pyb')");
            ResultSet rs = st.executeQuery("SELECT * FROM emp;");

            while(rs.next()){
                // System.out.println("Database Entry " + rs.getString(1));

                String name = rs.getString("name");
                String city = rs.getString("city");

                // System.out.printf("HI");
                System.out.printf("%-15s | %-5s\n",name,city);
            }
            conn.close();
        }catch(Exception e){
            e.printStackTrace();
        }
    }
}
