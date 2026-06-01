
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class Program5 {

    public static void main(String[] args) {

        try {
            // Class.forName("com.mysql.cj.jdbc.Driver");

            Connection con = DriverManager.getConnection(
                    "jdbc:mariadb://localhost:3306/java2026",
                    "root",
                    "java2026");

            con.setAutoCommit(false);

            Statement stmt = con.createStatement();

            stmt.executeUpdate("UPDATE accounts SET balance = balance - 500 WHERE id = 1");
            stmt.executeUpdate("UPDATE accounts SET balance = balance + 500 WHERE id = 2");

            con.commit();

            System.out.println("Transaction successful");

            con.close();

        } catch (Exception e) {
            System.out.println(e);
        }
    }
}