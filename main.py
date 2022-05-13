import reddit_reader
import models
import praw
# import db

reader = reddit_reader.RedditReader()

# class TestClass:
#   subreddit = "developersindia"
#   query_text = "python"
#   limit = 10

# testObject = TestClass()
# print(reader.get(testObject))

# response = []
# for result in reader.get(testObject):
#   if isinstance(result, praw.models.submission):
#     record = models.Record(result.title, result.url)
#   else:
#     record = models.Record(result.body, result.url)

#   response.append(record)





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