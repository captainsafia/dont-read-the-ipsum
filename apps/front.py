from flask import Flask, render_template, make_response

app = Flask(__name__, static_folder = '../static', template_folder="../templates")



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/docs/api")
def api_docs():
    return render_template("api_docs.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
