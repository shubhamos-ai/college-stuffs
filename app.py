from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/3-1")
def project_3_1():
    return render_template("21-02-2026/3-1 project.html")

@app.route("/3-2")
def project_3_2():
    return render_template("21-02-2026/3-2 project.html")

@app.route("/timpass")
def project_timepass():
    return render_template("21-02-2026/timepass.html")

if __name__ == "__main__":
    app.run(debug=True)
