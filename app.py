from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)


# =========================================================
# DATABASE CONNECTION
# =========================================================

def get_db_connection():

    return mysql.connector.connect(
        host="localhost",
        user="bptuser",
        password="9572",
        database="BPT"
    )


# =========================================================
# HOME
# =========================================================

@app.route("/")
def index():
    return render_template("index.html")


# =========================================================
# REGISTRATION PAGE
# =========================================================

@app.route("/register")
def register():
    return render_template("register.html")


# =========================================================
# OTHER NAVIGATION ROUTES
# =========================================================

@app.route("/courses")
def courses():
    return redirect(url_for("index") + "#courses")


@app.route("/prospectus")
def prospectus():
    return redirect(url_for("index") + "#prospectus")


@app.route("/achievements")
def achievements():
    return redirect(url_for("index") + "#achievements")


@app.route("/events")
def events():
    return redirect(url_for("index") + "#events")


@app.route("/professor")
def professor():
    return redirect(url_for("index") + "#professor")


# =========================================================
# SUBMIT REGISTRATION
# =========================================================

@app.route("/submit_registration", methods=["POST"])
@app.route("/submit", methods=["POST"])
def submit_registration():

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    mobile = request.form.get("mobile", "").strip()
    address = request.form.get("address", "").strip()
    college = request.form.get("college", "").strip()
    student_class = request.form.get("class", "").strip()


    # -----------------------------------------------------
    # BASIC VALIDATION
    # -----------------------------------------------------

    if not name or not email or not mobile:
        return """
        <h2>Required information is missing.</h2>
        <p>Please fill all required fields.</p>
        <a href="/register">Go Back</a>
        """, 400


    if not mobile.isdigit() or len(mobile) != 10:

        return """
        <h2>Invalid Mobile Number</h2>
        <p>Please enter a valid 10-digit mobile number.</p>
        <a href="/register">Go Back</a>
        """, 400


    conn = None
    cursor = None


    try:

        # -------------------------------------------------
        # DATABASE CONNECTION
        # -------------------------------------------------

        conn = get_db_connection()

        cursor = conn.cursor()


        # -------------------------------------------------
        # INSERT DATA
        # -------------------------------------------------

        sql = """
            INSERT INTO students
            (name, email, mobile, address, college, class)
            VALUES (%s, %s, %s, %s, %s, %s)
        """


        data = (
            name,
            email,
            mobile,
            address,
            college,
            student_class
        )


        cursor.execute(sql, data)


        # Save permanently
        conn.commit()


        # -------------------------------------------------
        # SUCCESS PAGE
        # -------------------------------------------------

        return render_template(
            "success.html",
            name=name
        )


    except mysql.connector.Error as error:

        if conn:
            conn.rollback()


        return render_template(
            "success.html",
            error=str(error)
        ), 500


    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )