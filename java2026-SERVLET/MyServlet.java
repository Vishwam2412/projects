import java.io.IOException;
import java.io.PrintWriter;
import java.net.http.HttpResponse;

import jakarta.servlet.*;
import jakarta.servlet.annotation.*;
import jakarta.servlet.http.*;
import java.sql.Connection;
import java.sql.Driver;
import java.sql.ResultSet;
import java.sql.Statement;
import java.sql.DriverManager;


// This maps the servlet to http://localhost:8080/hello
@WebServlet("/hello")
public class MyServlet extends HttpServlet {

    public void doGet(HttpServletRequest request, HttpServletResponse response) 
            throws ServletException, IOException {
                
                response.setContentType("text/html");
                PrintWriter out = response.getWriter();


                String url = "jdbc:mariadb://127.0.0.1:3306/java2026";
                String usr = "root";
                String passWord = "java2026";

                try{
                    // Class.forName("org.mariadb.jdbc.Driver");
                    Connection conn = DriverManager.getConnection(url,usr,passWord);
                    Statement stmt = conn.createStatement();
                    ResultSet rs = stmt.executeQuery("SELECT * FROM accounts");

                    out.println("<h3>--- DataBase Entries ---</h3>");
                    out.println("<table border='1'><tr><th>Acc No</th><th>Name</th><th>Balance</th></tr>");

                    while(rs.next()){
                        int acc = rs.getInt("acc_no");
                        String name = rs.getString("name");
                        Double bal = rs.getDouble("balance");
                        out.println("<tr><td>" + acc + "</td><td>" + name + "</td><td>" + bal + "</td></tr>");
                        // System.out.println("Account No: "+acc+" | Name: "+name+" | Balance: "+bal);
                    }
                    out.println("</table>");
                    rs.close();
                    stmt.close();
                    conn.close();

                }catch(Exception e){
                    e.printStackTrace();
                }
                
                out.println("<html><p>DataBase Connected</p></html>");


        
        out.println("<html><body>");
        out.println("<h2>Servlet Success!</h2>");
        out.println("<p>Running on Arch Linux with Tomcat 10 </p>");
        out.println("<p>This is the lupdated parameter</p>");
        out.println("</body></html>");
    }


    protected void doGet(HttpServletRequest req , HttpServletResponse res){
        
    }
}
