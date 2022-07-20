from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def greeting():
    return 'Give me a number (append number to URL)!'

@app.route('/<amount>')
def repeat(amount):
    amount = int(amount)
    return render_template("index.html", default=3, amount=amount)

@app.route('/<amount>/<color>')
def repeat_color(amount, color):
    amount = int(amount)
    color = f"background-color: {color}"
    print(color)
    return render_template("index.html", default=3, amount=amount, color=color)

if __name__=="__main__":
    app.run(debug=True)