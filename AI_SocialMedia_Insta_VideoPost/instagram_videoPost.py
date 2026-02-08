import os
import time
import uuid
import boto3
import requests
from dotenv import load_dotenv

load_dotenv()

IG_USER_ID = os.getenv("IG_USER_ID")
IG_ACCESS_TOKEN = os.getenv("IG_ACCESS_TOKEN")

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = "us-east-2"
S3_BUCKET = "sush-ig-media"

VIDEO_PATH = "final_instagram_post.mp4"  # local var

s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION,
)

def upload_to_s3(video_path):
    key = f"ig_uploads/{uuid.uuid4().hex}.mp4"
    print("1️⃣ Uploading MP4 to S3...")

    s3.upload_file(
        video_path,
        S3_BUCKET,
        key,
        ExtraArgs={"ContentType": "video/mp4"}  # ✅ NO ACL here
    )

    url = f"https://{S3_BUCKET}.s3.{AWS_REGION}.amazonaws.com/{key}"
    print("✅ Public video URL:\n", url)
    return url

def create_container(video_url):
    print("2️⃣ Creating IG REELS container...")

    url = f"https://graph.facebook.com/v19.0/{IG_USER_ID}/media"
    payload = {
        "media_type": "REELS",
        "video_url": video_url,
        "caption": "🚀 Built with AI + Python\n#AI #Tech #Reels",
        "access_token": IG_ACCESS_TOKEN
    }

    res = requests.post(url, data=payload)
    print("IG create response:", res.status_code, res.text)
    res.raise_for_status()
    return res.json()["id"]

def publish_container(creation_id):
    print("3️⃣ Publishing Reel...")
    url = f"https://graph.facebook.com/v19.0/{IG_USER_ID}/media_publish"
    payload = {"creation_id": creation_id, "access_token": IG_ACCESS_TOKEN}

    res = requests.post(url, data=payload)
    print("IG publish response:", res.status_code, res.text)
    res.raise_for_status()
    print("🎉 SUCCESS! Reel published.")

def main():
    video_url = upload_to_s3(VIDEO_PATH)
    creation_id = create_container(video_url)

    print("⏳ Waiting for Instagram to process video...")
    time.sleep(20)

    publish_container(creation_id)

if __name__ == "__main__":
    main()