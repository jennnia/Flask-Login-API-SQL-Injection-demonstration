# Flask-Login-API-SQL-Injection-demonstration

🌟 This Flask-based app demonstrates a SQL Injection (SQLi) vulnerability and its prevention. It provides two login endpoints: one vulnerable to SQL injection and one secure.

Vulnerable /login Endpoint: Uses concatenated SQL queries, allowing for SQL injection.
Secure /secure_login Endpoint: Uses parameterized queries to prevent SQL injection.
How to Use:
SQL Injection Attack:
Using curl, you can exploit the vulnerable endpoint with a payload like {"username": "admin", "password": "wrongpassword' OR '1'='1"} to bypass authentication.
Valid Login:
A valid login can be tested using curl with correct credentials: {"username": "admin", "password": "password123"}.
Invalid Login:
An invalid login attempt using curl with wrong credentials (e.g., {"username": "admin", "password": "wrongpassword"}) will return an error.
Additionally, I have created a small SQLi automation tool, utilizing hardcoded payloads for testing purposes.

❗️Note: This project is for educational purposes only. It is intended to demonstrate SQL injection vulnerabilities and how to secure applications from such attacks. It should not be used for malicious activities.
