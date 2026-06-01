import java.sql.*;

public class JDBCDiff {
    public static void main(String[] args) {
        String url = "jdbc:mariadb://localhost:3306/java2026";
        String user = "root";
        String pass = "java2026";

        try {
            Connection con = DriverManager.getConnection(url, user, pass);
            
            Statement stmt = con.createStatement();
            String sql1 = "INSERT INTO emp (id, name, city) VALUES (101, 'Arjun', 'Noida')";
            int rows1 = stmt.executeUpdate(sql1);
            System.out.println("Statement rows: " + rows1);
            stmt.close();

            String sql2 = "INSERT INTO emp (id, name, city) VALUES (?, ?, ?)";
            PreparedStatement pstmt = con.prepareStatement(sql2);
            pstmt.setInt(1, 102);
            pstmt.setString(2, "Ishita");
            pstmt.setString(3, "Greater Noida");
            
            int rows2 = pstmt.executeUpdate();
            System.out.println("PreparedStatement rows: " + rows2);
            
            pstmt.close();
            con.close();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}