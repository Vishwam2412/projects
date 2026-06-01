package regis;


import java.sql.*;

public class db_conn{
	    public static Connection getCon() throws Exception {
	        return DriverManager.getConnection(
	            "jdbc:mariadb://localhost:3306/java2026",
	            "root",
	            "java2026"
	        );
	    }
	}