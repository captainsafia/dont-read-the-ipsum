import praw

USER_AGENT = "web:com.do.not.read.the.ipsum:v0.0.1 (by /u/captainsafia)"
THREAD_IDS = {
    "neil_tyson" : "mateq",
    "barack_obamo" : "z1c9z"
}

client = praw.Reddit(user_agent = USER_AGENT)

def get_comments_from_name(name):
    submission_id = THREAD_IDS.get(name)
    if submission_id:
        submission = client.get_submission(submission_id = submission_id)
        return submission.comments
    else:
        raise Exception("Could not find submission ID for", name)
