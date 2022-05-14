import reddit_reader
import models

reader = reddit_reader.RedditReader()

# How to use RedditReader()
# 1. Create an object with 2 mandatory parameters
#    - subreddit - str format - name of subreddit - case sensitive
#    - query_text - str format - query you want to format
# 2. Optional Parameters
#    - sort_order - int - 0(default), 1(ascending-order), -1(descending-order)
#    - limit - int - 10(default), limits the number of submissions and no of submissions to match comments

#     Example
# -----------------
# reader.get(
#   models.RedditRequest(
#     subreddit="developersIndia",
#     query_text="javascript",
#     sort_order="Descending",
#   )
# )

print(reader.get(
  models.RedditRequest(
    subreddit="developersIndia",
    query_text="python",
    sort_order=1,
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