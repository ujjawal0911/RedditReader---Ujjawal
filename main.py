import reddit_reader
import models

reader = reddit_reader.RedditReader()


print(reader.get(
  models.RedditRequest(
    subreddit="developersIndia",
    query_text="javascript"
  )
))

# Task 1 -- get all reddit posts / comments that match a query
#
# reader.get(
#   models.RedditRequest(
#     subreddit="developersIndia",
#     query_text="python"
#   )
# )

# Task 2 -- use https://blog.replit.com/database for caching, so that
#           same request does not take time
#

# Task 3 -- extend client to include sort order and time sorting