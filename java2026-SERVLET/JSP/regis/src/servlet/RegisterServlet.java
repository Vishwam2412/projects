
package regis;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.Statement;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class RegisterServlet
 */
@WebServlet("/RegisterServlet")
public class RegisterServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        String name = request.getParameter("name");
        String email = request.getParameter("email");
        String course = request.getParameter("course");

        try {
            Connection con = db_conn.getCon();
            Statement st = con.createStatement();

            st.execute("DROP TABLE IF EXIST student");
            st.execute("CREATE TABLE student (    name VARCHAR(50),    email VARCHAR(50),    course VARCHAR(50));");
            st.close();

            PreparedStatement ps = con.prepareStatement(
                "INSERT INTO student VALUES(?,?,?)"
            );

            ps.setString(1, name);
            ps.setString(2, email);
            ps.setString(3, course);

            int i = ps.executeUpdate();

            if(i > 0){
                out.println("<h2>Registration Successful</h2>");
            } else {
                out.println("<h2>Failed</h2>");
            }

        } catch(Exception e){
            out.println(e);
        }
    }
}