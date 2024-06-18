from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "BUNI Jieo"

app.run(debug=True)