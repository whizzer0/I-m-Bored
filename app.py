from flask import Flask, render_template
app = Flask(__name__)

@app.route("/example", methods=["GET"])
def example():
    return render_template("example.html", data=None)

@app.route("/form", methods=["GET"])
def form():
    return render_template("form.html", data=None)

if __name__ == "__main__":
    app.run()
