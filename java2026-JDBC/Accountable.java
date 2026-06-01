package myapp;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class Accountable {

    public static void main(String[] args) {

        try {
            Class.forName("com.mysql.cj.jdbc.Driver");

            Connection con = DriverManager.getConnection(
                    "jdbc:mysql://localhost:3306/java2026",
                    "root",
                    "java2026");

            Statement st = con.createStatement();

            String query = "CREATE TABLE IF NOT EXISTS accounts ("
                    + "id INT PRIMARY KEY, "
                    + "name VARCHAR(50), "
                    + "balance DOUBLE)";

            st.executeUpdate(query);

            System.out.println("Accounts Table Created Successfully");

            con.close();

        } catch (Exception e) {
            System.out.println(e);
        }
    }
}