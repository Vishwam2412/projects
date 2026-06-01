
import java.sql.*;

public class Program9 {

    public static void main(String[] args) {

        Connection con = null;

        try {
            // Class.forName("com.mysql.cj.jdbc.Driver");

            con = DriverManager.getConnection(
                    "jdbc:mariadb://localhost:3306/java2026",
                    "root",
                    "java2026");

            con.setAutoCommit(false);

            Statement stmt = con.createStatement();

            stmt.executeUpdate("UPDATE accounts SET balance = balance - 300 WHERE id = 1");

            Savepoint sp = con.setSavepoint("SP1");

            stmt.executeUpdate("UPDATE accounts SET balance = balance + 300 WHERE id = 2");

            con.commit();

            System.out.println("Transaction successful");

            con.close();

        } catch (Exception e) {
            try {
                if (con != null) {
                    con.rollback();
                    System.out.println("Transaction rolled back");
                }
            } catch (Exception ex) {
                System.out.println(ex);
            }
            System.out.println(e);
        }
    }
}