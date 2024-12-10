import requests
import webbrowser

# Create a session to maintain cookies
session = requests.Session()

# Define the login URL
url = "http://testphp.vulnweb.com/login.php"

# Define the headers to mimic a real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Define the payload (correct format)
data = {
    "uname": "test",  # username as key-value pairs
    "pass": "test"    # password as key-value pairs
}

# POST request to log in with headers
response = session.post(url, data=data, headers=headers)

# Print the response text to check what happens after login
print(response.text)

# Check if login was successful by inspecting the response
if "Welcome" in response.text:  # Assuming the page contains 'Welcome' on successful login
    print("Login successful!")
else:
    print("Login failed. Check your credentials.")

# Get the user info page after successful login
r = session.get('http://testphp.vulnweb.com/userinfo.php')

# Save the page content to a file
with open('file.html', 'wb') as file:
    file.write(r.content)

# Open the saved file in the web browser
webbrowser.open('file.html')
