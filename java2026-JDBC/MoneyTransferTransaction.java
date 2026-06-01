
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class MoneyTransferTransaction {

    public static void main(String[] args) {

        Connection con = null;

        try {
            Class.forName("com.mysql.cj.jdbc.Driver");

            con = DriverManager.getConnection(
                    "jdbc:mysql://localhost:3306/java2026",
                    "root",
                    "java2026");

            con.setAutoCommit(false);

            Statement st = con.createStatement();

            st.executeUpdate("UPDATE accounts SET balance = balance - 1000 WHERE id = 1");

            st.executeUpdate("UPDATE accounts SET balance = balance + 1000 WHERE id = 2");

            con.commit();

            System.out.println("Money Transferred Successfully");

            con.close();

        } catch (Exception e) {
            try {
                if (con != null) {
                    con.rollback();
                    System.out.println("Transaction Rolled Back");
                }
            } catch (Exception ex) {
                System.out.println(ex);
            }

            System.out.println(e);
        }
    }
}