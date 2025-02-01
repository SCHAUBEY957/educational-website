from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Connect to the MySQL database
def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='bptuser',       # replace with your MySQL username
        password='9572',  # replace with your MySQL password
        database='BPT'         # your database name
    )
    return conn

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/submit", methods=["POST"])
def submit():
    data = (
        request.form["name"],
        request.form["email"],
        request.form["mobile"],
        request.form["address"],
        request.form["college"],
        request.form["class"],
    )
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO students (name, email, mobile, address, college, class)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, data)
    
    conn.commit()
    cursor.close()
    conn.close()

    return "Registration successful!"

if __name__ == "__main__":
    app.run(debug=True)
