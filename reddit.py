import praw
import re
import time 
import pandas as pd


ticker_df = pd.read_csv('tickers.csv')
print(ticker_df)

reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent="<console:databot:1.0>",
)

subreddit = reddit.subreddit("wallstreetbets")

for submission in subreddit.hot(limit=100):
        print("**************")
        print(submission.title)



        for comment in submission.comments:
            if hasattr(comment,"body"):
                comment_activate = comment.body.lower()
                if "!data" in comment_activate:
                    print("---------")
                    print(comment.body)

        
