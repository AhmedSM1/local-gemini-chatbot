

from dotenv import load_dotenv
import os

import google.generativeai as genai
from google.generativeai import types 

load_dotenv()  # Loads .env file into environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

def gemini_response(prompt:str) -> str:  
    resp = model.generate_content(
        prompt,
        generation_config=types.GenerationConfig(  # ← use generation_config
            max_output_tokens=512,
            temperature=0.7,
            top_p=0.95,
        ),
    )
    return resp.text