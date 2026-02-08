from langchain_openai import ChatOpenAI
#from openai import OpenAI
from dotenv import load_dotenv
import os

# Load the environment variables from .env
load_dotenv()

# Initialize the OpenAI LLM with GPT-4o
llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), model="gpt-4o")
#llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Function to generate caption from UGC
def generate_caption(ugc):
  prompt = f"Write a short, friendly social media caption based on this testimonial: '{ugc['testimonial']}'. Tag the user {ugc['user_handle']}."
  
  # Make the API call
  response = llm.invoke(prompt)

  # Extract only the content part of the response
  caption = response.content

  print(f"\nGenerated Caption: {caption}\n")
  return caption