
import java.sql.*;

public class Program8 {

    public static void main(String[] args) {

        try {
            // Class.forName("com.mysql.cj.jdbc.Driver");

            Connection con = DriverManager.getConnection(
                    "jdbc:mariadb://localhost:3306/java2026",
                    "root",
                    "java2026");

            CallableStatement cs = con.prepareCall("{call totalSalary(?)}");

            cs.setString(1, "IT");

            ResultSet rs = cs.executeQuery();

            while (rs.next()) {
                System.out.println("Total Salary: " + rs.getInt("total"));
            }

            con.close();

        } catch (Exception e) {
            System.out.println(e);
        }
    }
}