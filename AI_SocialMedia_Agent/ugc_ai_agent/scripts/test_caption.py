import requests
import os
import json
from caption_generator import generate_caption
from image_generator import generate_image_from_caption
#from reddit_poster import post_to_reddit
from instagram_poster import create_media_object, publish_media_object

# Load UGC (User-Generated Content) data from a local JSON file
with open('../data/ugc_data.json', 'r') as file:
  data = json.load(file)      # Parse the JSON file into a Python dictionary

ugc_entries = data['ugc']     # Extract the list of UGC entries from the dictionary

# Loop through all UGC entries and Generate Captions for each
for ugc_entry in ugc_entries:
  caption = generate_caption(ugc_entry)                     # Generate a social media caption based on the UGC
  image_url = generate_image_from_caption(caption)          # Generate an image from the caption using DALL·E 3
  #image_url = "https://drive.google.com/file/d/1AZSuQskYs5bXDxUAjVN1ok-xQPGhpZfW/view?usp=drive_link"
  
  #file_id = "1AZSuQskYs5bXDxUAjVN1ok-xQPGhpZfW"
  #image_url = f"https://drive.google.com/uc?export=download&id=1AZSuQskYs5bXDxUAjVN1ok"

  # Download image from Azure blob URL
  local_image_path = "temp_image.png"
  response = requests.get(image_url)
  with open(local_image_path, "wb") as f:
    f.write(response.content)

  # Post to Reddit
  #reddit_post_url = post_to_reddit("u_" + os.getenv("REDDIT_USERNAME"), caption, local_image_path)
  
  # POST TO INSTAGRAM
  media_response = create_media_object(image_url, caption)
  print("Media response:", media_response)

  if "id" in media_response:
     publish_response = publish_media_object(media_response["id"])
     print("Publish response:", publish_response)
  else:
     print("⚠️ Failed to create Instagram media")

  print("Final Caption:", caption)
  print("Image URL:", image_url)
  #print("Reddit Post URL:", reddit_post_url)
  print('-' * 80) # Just to separate each caption visually in the terminal
  

