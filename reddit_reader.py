# https://praw.readthedocs.io/en/stable/getting_started/quick_start.html
import praw
from replit import db

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

    # Create a search_query for caching
    search_query = f"subreddit='{subreddit}' limit={limit} query_text='{query_text}'"

    # Search if in database - if not use the API
    if search_query in db:
      return db[search_query]
    else:
      results_list = self.get_submissions(subreddit, query_text, limit) + self.get_comments(subreddit, query_text, limit)

      # Creating a list for RedditResponse
      responseList =[]

      # Creating Record instances extracting link and text
      for result in results_list:
        if isinstance(result, praw.models.Submission):
          record = {'text':result.title, 'link':result.url}
        else:
          record = {'text':result.body, 'link':result.permalink}

        # Appending each dictionary in List
        responseList.append(record)

      db[search_query] = responseList
      return responseList
      

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