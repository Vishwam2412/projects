import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class JDBCFetch {
    public static void main(String[] args) {
        String url = "jdbc:mariadb://localhost:3306/java2026";
        String user = "root";
        String pass = "java2026";

        try {
            Connection con = DriverManager.getConnection(url, user, pass);            
            Statement stmt = con.createStatement();
            String sql = "SELECT id, name, city FROM emp";
            
            ResultSet rs = stmt.executeQuery(sql);

            System.out.println("ID\tNAME\t\tCITY");
            System.out.println("-----------------------------------");

            while (rs.next()) {
                int id = rs.getInt("id");
                String name = rs.getString("name");
                String city = rs.getString("city");
                
                System.out.println(id + "\t" + name + "\t\t" + city);
            }

            rs.close();
            stmt.close();
            con.close();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}