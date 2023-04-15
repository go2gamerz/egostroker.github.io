from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/feedback", methods=["POST"])
def feedback():
    text = request.form["text"]
    return render_template("feedback.html", text=text)

if __name__ == "__main__":
    app.run(debug=True)
