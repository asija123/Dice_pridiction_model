from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Form se values le lo
        a = request.form.get("a")
        b = request.form.get("b")
        c = request.form.get("c")
        
        # Tumhara prediction logic yahan ayega
        prediction = [int(a), int(b), int(c), 12]  # Bas example ke liye

        return render_template("index.html", prediction=prediction)

    return render_template("index.html")

if __name__ == "__main__":
    app.run()
