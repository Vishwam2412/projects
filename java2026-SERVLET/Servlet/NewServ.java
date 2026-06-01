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


@WebServlet("/rap")
public class NewServ extends HttpServlet{
    // public static void main( String []args){
        
    // }

    public void doGet(HttpServletRequest req , HttpServletResponse res)
        throws ServletException,IOException{
            Cookie cookie =  new Cookie("name","harper")  ;
            res.addCookie(cookie);
            res.setContentType("text/html");
            res.getWriter().println("Cookie Created Successfully");
        }
}
