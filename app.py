from flask import Flask, render_template, request
from api import lookUpEventFul
app = Flask(__name__)
app.debug = True

@app.route("/", methods=["GET"])
def example():
    return render_template("example.html", data=None)

@app.route("/form", methods=["GET"])
def form():
    return render_template("form.html", data=None)

@app.route("/results", methods=["POST"])
def results():
	results = lookUpEventFul(request.form["town"])
	output = ""

	for event in results.iter('events'):
		for node in event:
			output += str(node.tag) + " - " + str(node.attrib) + " - " + str(node.find('title').text)


	return render_template("results.html", data=output)
	
if __name__ == "__main__":
    app.run()
