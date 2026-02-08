import os
import requests
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("IG_ACCESS_TOKEN")
USER_ID = os.getenv("IG_USER_ID")

def create_media_object(image_url, caption):
    endpoint = f"https://graph.facebook.com/v18.0/{USER_ID}/media"
  
    payload = {
          "image_url": image_url,
          "caption": caption,
          "access_token": ACCESS_TOKEN
      }
    response = requests.post(endpoint, data=payload)
    return response.json()

def publish_media_object(media_id):
    endpoint = f"https://graph.facebook.com/v18.0/{USER_ID}/media_publish"
    payload = {
        "creation_id": media_id,
        "access_token": ACCESS_TOKEN
    }
    response = requests.post(endpoint, data=payload)
    return response.json()