
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class Program3 {

    public static void main(String[] args) {

        try {
            // Class.forName("com.mysql.cj.jdbc.Driver");

            Connection con = DriverManager.getConnection(
                    "jdbc:mariadb://localhost:3306/java2026",
                    "root",
                    "java2026");

            Statement stmt = con.createStatement();

            stmt.executeUpdate(
                "CREATE TABLE IF NOT EXISTS Students(id INT, name VARCHAR(50), age INT, grade VARCHAR(10))"
            );

            System.out.println("Students table created successfully");

            con.close();

        } catch (Exception e) {
            System.out.println(e);
        }
    }
}