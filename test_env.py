import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
print(f"API Key found: {api_key is not None}")
if api_key:
    print(f"API Key starts with: {api_key[:15]}...")
    print(f"API Key length: {len(api_key)}")
else:
    print("API Key is None - check your .env file")