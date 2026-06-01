
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class Program2 {

    public static void main(String[] args) {

        try {
            // Class.forName("com.mysql.cj.jdbc.Driver");

            Connection con = DriverManager.getConnection(
                    "jdbc:mariadb://localhost:3306/java2026",
                    "root",
                    "java2026");

            Statement stmt = con.createStatement();

            stmt.executeUpdate(
                "CREATE TABLE IF NOT EXISTS emp(id INT, name VARCHAR(50), city VARCHAR(50))"
            );

            stmt.executeUpdate("INSERT INTO emp VALUES (1, 'Vivek', 'Delhi')");
            stmt.executeUpdate("INSERT INTO emp VALUES (2, 'Rahul', 'Noida')");

            System.out.println("Table created and data inserted successfully");

            con.close();

        } catch (Exception e) {
            System.out.println(e);
        }
    }
}