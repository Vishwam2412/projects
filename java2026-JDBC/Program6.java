import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;

public class Program6 {

    public static void main(String[] args) {

        try {
            // Class.forName("com.mysql.cj.jdbc.Driver");

            Connection con = DriverManager.getConnection(
                    "jdbc:mariadb://localhost:3306/java2026",
                    "root",
                    "java");

            String query = "DELETE FROM Students WHERE grade < ?";

            PreparedStatement ps = con.prepareStatement(query);

            ps.setString(1, "B");

            int rows = ps.executeUpdate();

            System.out.println(rows + " records deleted");

            con.close();

        } catch (Exception e) {
            System.out.println(e);
        }
    }
}