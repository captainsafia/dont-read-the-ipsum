from flask import Flask, render_template, request, jsonify, redirect
import reddit

api = Flask(__name__)

@api.route("/api")
def index():
    return "API stats"

@api.route("/api/comment/ipsum/twitter/<source>")
def ipsum_from_twitter():
    pass

@api.route("/api/comment/reddit", methods=["POST"])
def ipsum_from_reddit():
    data = request.form
    count = data.get("count")
    count_type = data.get("count_type")
    source = data.get("source")

    if count and count_type and source:
        comments = reddit.get_comments_from_short_url(source)
        comments_text = reddit.get_text_from_comments(int(count), 
                count_type, comments)
        text = reddit.get_jumbled_text(comments_text)
    output = {"text": text}
    return jsonify(**output)

if __name__ == "__main__":
	api.run(debug=True, host='0.0.0.0')
