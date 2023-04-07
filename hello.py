from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    i=2
    j=3
    k=i+j
    return (f"<p>Hello, World!</p> {k}")
