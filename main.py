import csv
import os
from flask import Flask, render_template, request

app = Flask(__name__)

CSV_FILE = "data.csv"

# Create file with header if it doesn't exist
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Actual"])

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

            # Save to CSV
            try:
                with open(CSV_FILE, mode="a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow([actual])
                message = f"Actual value {actual} saved to CSV successfully!"
            except Exception as e:
                message = f"Error saving to CSV: {str(e)}"

            return render_template("index.html", message=message)

    return render_template("index.html")

if __name__ == "__main__":
    app.run()
