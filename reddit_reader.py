# https://praw.readthedocs.io/en/stable/getting_started/quick_start.html
import praw

# Configuring the Praw API
redditAPI = praw.Reddit(
    client_id="qadPzWVI75BJlRjc-SOSnw",
    client_secret="8fMXahzWU1nuIl_6g-6_IlpDL-48DA",
    user_agent="test-app scraper by u/Extreme-Rooster-868",
)

class RedditReader():
  # Get Function to get all data
  def get(self, object):
    subreddit = object.subreddit
    query_text = object.query_text
    limit = object.limit

    return self.get_submissions(subreddit, query_text, limit) + self.get_comments(subreddit, query_text, limit)

  # Function to retrieve all submissions
  def get_submissions(self, subreddit, query_text, limit):
    return list(redditAPI.subreddit(subreddit).search(query_text, limit=limit))

  # Function to retrieve all comments
  def get_comments(self, subreddit, query_text, limit):
    results = []

    # Getting each submission and retrieveing all the comments from each submission
    for submission in redditAPI.subreddit(subreddit).top(limit=limit):

      # Replace_more to convert MoreComment object into Comment Tree
      submission.comments.replace_more(limit=limit, threshold=0)
      flat_comments = submission.comments.list()

      for comment in flat_comments:
        if query_text in comment.body:
          results.append(comment)

    return results