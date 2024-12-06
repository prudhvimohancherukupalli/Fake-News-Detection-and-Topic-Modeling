import os
import requests
from dotenv import load_dotenv, find_dotenv

# Load environment variables from .env file
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# Fetch the Hugging Face API Key
API_KEY = os.getenv("HUGGINGFACE_API_KEY")
if not API_KEY:
    print("API key not found.")
    exit()

# Test API Request
model_name = "bert-base-uncased"
payload = {"inputs": "Hello, world!"}
url = f"https://api-inference.huggingface.co/models/{model_name}"
headers = {"Authorization": f"Bearer {API_KEY}"}

response = requests.post(url, headers=headers, json=payload)
if response.status_code == 200:
    print("Test API Key Result:", response.json())
else:
    print(f"Error: {response.status_code}, {response.json()}")
