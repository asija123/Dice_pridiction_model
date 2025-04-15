from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if "predict" in request.form:
            # Predict button clicked
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
            # Save Actual button clicked
            actual = request.form.get("actual")

            print(f"Saving actual value: {actual}")

            try:
                actual = int(actual)
            except (TypeError, ValueError):
                return "Invalid input. Please enter valid actual number."

            # Save logic (DB, CSV, etc.) can go here
            message = f"Actual value {actual} saved successfully!"
            return render_template("index.html", message=message)

    return render_template("index.html")

if __name__ == "__main__":
    app.run()
