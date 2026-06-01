
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;

public class Program7 {

    public static void main(String[] args) {

        try {
            // Class.forName("com.mysql.cj.jdbc.Driver");

            Connection con = DriverManager.getConnection(
                    "jdbc:mariadb://localhost:3306/java2026",
                    "root",
                    "java2026");

            String query = "INSERT INTO Students VALUES (?, ?, ?, ?)";

            PreparedStatement ps = con.prepareStatement(query);

            ps.setInt(1, 4);
            ps.setString(2, "Neha");
            ps.setInt(3, 23);
            ps.setString(4, "A");
            ps.addBatch();

            ps.setInt(1, 5);
            ps.setString(2, "Arjun");
            ps.setInt(3, 24);
            ps.setString(4, "B");
            ps.addBatch();

            ps.executeBatch();

            System.out.println("Batch inserted successfully");

            con.close();

        } catch (Exception e) {
            System.out.println(e);
        }
    }
}