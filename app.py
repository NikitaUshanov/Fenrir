from flask import Flask, render_template
#test

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template("home/home.html")

if __name__ == '__main__':
    app.run(debug=True)