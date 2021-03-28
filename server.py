from flask import Flask

PORT = 8000
MESSAGE = "Welcome to Project 1 \n project is running successfully \n this is line 3"

app = Flask(__name__)


@app.route("/")
def root():
    result = MESSAGE.encode("utf-8")
    return result


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
