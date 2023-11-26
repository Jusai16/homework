from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calc/<type1>")
def calc(type1):
    n1 = 55
    n2 = 108
    with open ("my_file", "w") as file:
        file.write("n1 = 55, n2 = 108")
    return render_template("calc.html",
                           num1 = n1,
                           num2 = n2,
                           calc_type = type1)



app.run(debug = True)