import praw
import string
import random
try:
    import urllib.parse as urlparse
except ImportError:
    from urlparse import urlparse

USER_AGENT = "web:com.do.not.read.the.ipsum:v0.0.1 (by /u/captainsafia)"

client = praw.Reddit(user_agent = USER_AGENT)

def get_id_from_url(url):
    """
    Gets the ID associated with a Reddit submission
    """
    try:
        parsed = urlparse.urlparse(url)
        submission_id = parsed.path.strip("/")
        return submission_id
    except:
        raise Exception("Could not find submission ID for", url)

def get_comments_from_short_url(url):
    """
    Returns the comment submissions from a particular URL
    """
    submission_id = get_id_from_url(url)
    if submission_id:
        submission = client.get_submission(submission_id = submission_id)
        return submission.comments

def get_text_from_comment(comment):
    """
    Get cleaned body from comment.
    """
    if comment.body:
        body = comment.body
        exclude = set(string.punctuation.replace("'", ""))
        body = "".join(char for char in body if char not in exclude)
        body = " ".join(word for word in body.split(" ") if not word.startswith("http"))
        return body
    else:
        raise Exception("Could not find body for comment", comment.id)

def counter_helper_partial(count_type):
    def word_counter(text):
        text = text.split(" ")
        return len(text)

    def char_counter(text):
        return len(text)

    if count_type == "word":
        return word_counter
    elif count_type == "char":
        return char_counter
    else:
        raise Exception("Unrecognized count_type: ", count_type)

def truncate_content(content, expected, actual):
    """
    Truncate the content from the actual length to the expected length.
    """
    truncated = content[0:min(actual, expected)]
    return truncated

def get_text_from_comments(count, count_type, comments):
    """
    Get up to count of count_type from comments.
    """
    aggregated = ""
    random.shuffle(comments)
    for comment in comments:
        if isinstance(comment, praw.objects.MoreComments):
            comments = comment.comments()
            continue

        content = get_text_from_comment(comment)
        try:
            counter_helper = counter_helper_partial(count_type)
        except:
            counter_helper = counter_helper_partial("word")

        actual_count = counter_helper(content)
        if actual_count > count:
            aggregated += (truncate_content(content, actual_count, count) + " ")
            break
        else:
            aggregated += (content + " ")
    return aggregated

def get_jumbled_text(text):
    """
    Return jumpled version of text.
    """
    text = text.split(" ")
    jumbled = ""

    while len(text) > 0:
        word = random.choice(text)
        del text[text.index(word)]
        jumbled += (word + " ")

    return jumbled.strip()
