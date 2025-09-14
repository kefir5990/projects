from flask import Flask
from resources import Entry

app = Flask("NAME")

@app.route("/")
def hello_world():
    return []

if __name__ == "__main__":
    app.run("0.0.0.0", port = 8000, debug=False)