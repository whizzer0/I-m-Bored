from flask import Flask, render_template
app = Flask(__name__)

@app.route("/example", methods=["GET"])
def hello():
    return render_template("example.html", data=None)

if __name__ == "__main__":
    app.run()
