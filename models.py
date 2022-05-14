from typing import List, Optional as O
# from enum import Enum
# from typing import Mapping, Any
from pydantic import BaseModel

# TODO: Feel free to edit / add to these as required.


class RedditRequest(BaseModel):
    subreddit: O[str]
    limit: O[int] = 10
    query_text: O[str]
    sort_order: O[int] = 0


class Record(BaseModel):
    text: O[str]
    link: O[str]


class RedditResponse(BaseModel):
    records: O[List[Record]]
