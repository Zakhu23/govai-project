from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

def get_db():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "database.db")
    return sqlite3.connect(db_path)

def init_db():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS schemes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        description TEXT,
        type TEXT,
        min_age INTEGER,
        max_age INTEGER,
        income REAL,
        occupation TEXT,
        state TEXT,
        qualification TEXT,
        apply_link TEXT
    )
    """)

    conn.commit()
    conn.close()

# 🔥 AUTO RUN
init_db()

@app.route("/", methods=["GET", "POST"])
def home():
    results = []

    if request.method == "POST":
        age = int(request.form["age"])
        income = float(request.form["income"])
        occupation = request.form["occupation"]
        state = request.form["state"]
        qualification = request.form["qualification"]

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT name, description, type, apply_link
            FROM schemes
            WHERE 
                (? BETWEEN min_age AND max_age)
                AND (income IS NULL OR ? <= income)
                AND (occupation = ? OR occupation = 'any')
                AND (state = ? OR state = 'all states')
                AND (? = 'any' OR qualification = ? OR qualification = 'any')
        """, (age, income, occupation, state, qualification, qualification))

        results = cursor.fetchall()
        conn.close()

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run()