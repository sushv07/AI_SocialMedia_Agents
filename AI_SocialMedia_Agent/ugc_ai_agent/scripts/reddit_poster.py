import praw
from dotenv import load_dotenv
import os

load_dotenv()

# Reddit Authentication
reddit = praw.Reddit(
  client_id=os.getenv("REDDIT_CLIENT_ID"),
  client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
  username=os.getenv("REDDIT_USERNAME"),
  password=os.getenv("REDDIT_PASSWORD"),
  user_agent="ugc_agent",
  read_only=False
)



def post_to_reddit(subreddit_name, title, image_path):
  subreddit = reddit.subreddit(subreddit_name)
  try:
    submission = subreddit.submit_image(title=title, image_path=image_path)
    print(f"\nReddit Post URL: {submission.url}\n")
    return submission.url
  except Exception as e:
    print(f"X Error posting to Reddit: {e}")
    return None

