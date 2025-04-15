# import csv
# import sqlite3
# import os
# DB_FILE = "data.db"

# from flask import Flask, render_template, request

# app = Flask(__name__)
# def init_db():
#     conn = sqlite3.connect(DB_FILE)
#     c = conn.cursor()
#     c.execute('''CREATE TABLE IF NOT EXISTS predictions (actual INTEGER)''')
#     conn.commit()
#     conn.close()

# init_db()


# CSV_FILE = "predictions.csv"

# # Create file with header if it doesn't exist
# if not os.path.exists(CSV_FILE):
#     with open(CSV_FILE, mode="w", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow(["Actual"])

# @app.route("/", methods=["GET", "POST"])
# def home():
#     if request.method == "POST":
#         if "predict" in request.form:
#             a = request.form.get("a")
#             b = request.form.get("b")
#             c = request.form.get("c")

#             print(f"Predicting with values - a: {a}, b: {b}, c: {c}")

#             try:
#                 prediction = [int(a), int(b), int(c), 18]  # Dummy prediction
#             except (TypeError, ValueError):
#                 return "Invalid input. Please enter valid numbers."

#             return render_template("index.html", prediction=prediction)

#         elif "submit_actual" in request.form:
#             actual = request.form.get("actual")

#             try:
#                 actual = int(actual)
#             except (TypeError, ValueError):
#                 return "Invalid input. Please enter valid actual number."

#             # Save to CSV
#             try:
#                 conn = sqlite3.connect(DB_FILE)
#                 c = conn.cursor()
#                 c.execute("INSERT INTO predictions (actual) VALUES (?)", (actual,))
#                 conn.commit()
#                 conn.close()

#                 message = f"Actual value {actual} saved to CSV successfully!"
#             except Exception as e:
#                 message = f"Error saving to CSV: {str(e)}"

#             return render_template("index.html", message=message)

#     return render_template("index.html")

# if __name__ == "__main__":
#     app.run()

import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)
DB_FILE = "data.db"

# Initialize the database
def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS predictions (actual INTEGER)''')
    conn.commit()
    conn.close()

# Initialize DB on app start
init_db()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if "predict" in request.form:
            a = request.form.get("a")
            b = request.form.get("b")
            c = request.form.get("c")

            print(f"Predicting with values - a: {a}, b: {b}, c: {c}")

            try:
                prediction = [int(a), int(b), int(c), 18]  # Dummy prediction
            except (TypeError, ValueError):
                return "Invalid input. Please enter valid numbers."

            return render_template("index.html", prediction=prediction)

        elif "submit_actual" in request.form:
            actual = request.form.get("actual")

            try:
                actual = int(actual)
            except (TypeError, ValueError):
                return "Invalid input. Please enter valid actual number."

            # Save to database
            try:
                conn = sqlite3.connect(DB_FILE)
                c = conn.cursor()
                c.execute("INSERT INTO predictions (actual) VALUES (?)", (actual,))
                conn.commit()
                conn.close()

                message = f"Actual value {actual} saved to database successfully!"
            except Exception as e:
                message = f"Error saving to database: {str(e)}"

            return render_template("index.html", message=message)

    return render_template("index.html")

if __name__ == "__main__":
    app.run()

