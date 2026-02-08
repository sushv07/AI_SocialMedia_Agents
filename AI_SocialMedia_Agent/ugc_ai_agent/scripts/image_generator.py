from openai import OpenAI         # OpenAI SDK for API access
from dotenv import load_dotenv    # To load API key from .env file
import os                         # To interact with environment variables

# Load environment variables from a .env file
load_dotenv()

# Initialize the OpenAI client with your secret API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Function to generate an image using a caption as the prompt
def generate_image_from_caption(caption):

  # Call OpenAI's DALL·E 3 model with the caption as the image prompt
  response = client.images.generate(
      model="dall-e-3",
      prompt=caption,
      n=1,                  # Generate a single image
      size="1024x1024"      # Set the output image resolution (square image)
  )
  
  # Extract the image URL from the API response
  image_url = response.data[0].url

  # Print the generated image URL for reference
  print(f"\nGenerated Image URL: {image_url}\n")
  
  return image_url
