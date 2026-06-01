
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class Program4 {

    public static void main(String[] args) {

        try {
            // Class.forName("com.mysql.cj.jdbc.Driver");

            Connection con = DriverManager.getConnection(
                    "jdbc:mariadb://localhost:3306/java2026",
                    "root",
                    "java2026");

            Statement stmt = con.createStatement();

            stmt.executeUpdate("INSERT INTO Students VALUES (1,'Aman',20,'A')");
            stmt.executeUpdate("INSERT INTO Students VALUES (2,'Riya',21,'B')");
            stmt.executeUpdate("INSERT INTO Students VALUES (3,'Karan',22,'C')");

            System.out.println("Multiple records inserted successfully");

            con.close();

        } catch (Exception e) {
            System.out.println(e);
        }
    }
}