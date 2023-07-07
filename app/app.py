#!python
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")

@app.route('/results', methods=['POST'])
def results():
    name = ""
    weight = ""
    height = ""
    name = request.form.get('username')
    weight = request.form.get('userweight')
    height = request.form.get('userheight')
    try:
        calWeight = float(weight)
        calHeight = float(height)
        result = round(calWeight / calHeight**2 * 703, 1)
        return render_template("results.html", name=name, weight=weight, height=height, result=result)
    except:
        return render_template('index.html',error="Incomplete Data")


if __name__ == "__main__":
    app.run(debug=True)
