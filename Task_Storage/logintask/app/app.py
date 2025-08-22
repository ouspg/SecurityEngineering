from flask import Flask, render_template, request, redirect, url_for
import os
import mysql.connector

app = Flask(__name__)

# hardcoded credentials for testing
# users = {
#     "admin": "admin1",
#     "user": "user1"
# }
#

# mysql connection config (modify for more secure password)
db_config = {
    'host': os.environ.get('DB_HOST', 'localhost'),
    'user': os.environ.get('DB_USER', 'root'),
    'password': os.environ.get('DB_PASSWORD', 'rootlogin'),
    'database': os.environ.get('DB_NAME', 'login')
}

# Check credentials versus the mysql database
def check_credentials(username, password):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result is not None
    except mysql.connector.Error as err:
        print("Database error:", err)
        return False

# flask
@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if check_credentials(username, password):
        return render_template('success.html', username=username)
    else:
        error = "Invalid username or password"
        return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)

