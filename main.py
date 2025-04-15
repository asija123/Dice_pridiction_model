from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        a = request.form.get("a")
        b = request.form.get("b")
        c = request.form.get("c")

        print(f"Received values - a: {a}, b: {b}, c: {c}")

        try:
            prediction = [int(a), int(b), int(c), 18]
        except (TypeError, ValueError) as e:
            print(f"Error in conversion: {e}")
            return "Invalid input. Please enter valid numbers."

        return render_template("index.html", prediction=prediction)

    return render_template("index.html")

if __name__ == "__main__":
    app.run()
