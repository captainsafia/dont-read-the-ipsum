from flask import Flask, render_template, make_response

app = Flask(__name__, template_folder="../templates")

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
