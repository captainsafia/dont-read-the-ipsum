import praw
import string

USER_AGENT = "web:com.do.not.read.the.ipsum:v0.0.1 (by /u/captainsafia)"
THREAD_IDS = {
    "neil_tyson" : "mateq",
    "barack_obamo" : "z1c9z"
}

client = praw.Reddit(user_agent = USER_AGENT)

def get_comments_from_name(name):
    """
    Get comments from submission by name.
    """
    submission_id = THREAD_IDS.get(name)
    if submission_id:
        submission = client.get_submission(submission_id = submission_id)
        return submission.comments
    else:
        raise Exception("Could not find submission ID for", name)

def get_text_from_comment(comment):
    """
    Get cleaned body from comment.
    """
    if comment.body:
        body = comment.body
        body = body.translate(string.maketrans("", ""), string.punctuation)
        body = body.lower()
        return body
    else:
        raise Exception("Could not find body for comment", comment.id)

def get_text_from_comments(count, count_type, comments):
    """
    Get up to count of count_type from comments.
    """
    aggregated = ""
    for comment in comments:
        content = get_text_from_comment(comment)
        if counter_helper(content) > count:
            aggregated += truncate_content(content)
        else:
            aggregated += content
    return aggregated
