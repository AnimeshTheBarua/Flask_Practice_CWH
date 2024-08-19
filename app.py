from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    # return "<p>Hello, World !</p>"
    return render_template('index.html')

@app.route('/products')
def products():
    return "<h1>This Page is for Products !</h1>"

if __name__ == "__main__":
    app.run(debug=True, port=8000)