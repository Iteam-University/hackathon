from flask import flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.methods == "POST":
        test=request.form["news"]
        #appel fonction predict avec l'input
        if test=="real":
            return render_template("real.html")
        else:
            return render_template("fake.html")
    else:
        return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)