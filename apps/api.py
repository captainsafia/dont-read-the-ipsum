from flask import Flask, render_template, request, jsonify, redirect
import reddit
import twitter
import nyt

api = Flask(__name__)

@api.route("/")
def index():
    return "API stats"

@api.route("/comment/ipsum/twitter", methods = ["POST"])
def ipsum_from_twitter():
    data = request.form
    count = data.get("count")
    count_type = data.get("count_type")
    source = data.get("source")
    tweets_or_replies = data.get("tweets_or_replies")
    if tweets_or_replies == 'replies':
        tweets = twitter.get_replies_to_user(int(count), source)
        cleaned_tweets = twitter.clean_up_text(tweets,int(count))
        jumbled_text = twitter.get_jumbled_text(cleaned_tweets)
    else:
        tweets = twitter.get_tweets_from_user(int(count), source)
        cleaned_tweets = twitter.clean_up_text(tweets, int(count))
        jumbled_text = twitter.get_jumbled_text(cleaned_tweets)
    output = {"text": jumbled_text}
    return jsonify(**output)

@api.route("/comment/ipsum/reddit", methods=["POST"])
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

@api.route("/comment/ipsum/nyt", methods = ["POST"])
def ipsum_from_nyt():
    data = request.form
    count = data.get("count")
    source = data.get("source")
    jumbled_text = ""
    json_paragraphs = nyt.get_json(source)
    paragraphs = nyt.json_to_string(json_paragraphs)
    cleaned_paragraphs = nyt.clean_up_text(paragraphs, int(count))
    jumbled_paragraphs = nyt.get_jumbled_text(cleaned_paragraphs)
    output = {"text": jumbled_paragraphs}
    return jsonify(**output)





if __name__ == "__main__":
	api.run(debug=True, host='0.0.0.0')
