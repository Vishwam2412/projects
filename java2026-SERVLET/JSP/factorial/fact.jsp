<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <title>Factorial Result</title>
</head>
<body>
    <%
        // 1. Get the parameter from the form
        String input = request.getParameter("num");
        
        if (input != null) {
            int n = Integer.parseInt(input);
            long factorial = 1;
            
            // 2. Logic to calculate factorial
            for (int i = 1; i <= n; i++) {
                factorial *= i;
            }
    %>
            <h3>The Factorial of <%= n %> is: <%= factorial %></h3>
    <%
        } else {
    %>
            <h3>Please enter a valid number.</h3>
    <%
        }
    %>
    <br>
    <a href="index.html">Back to Home</a>
</body>
</html>