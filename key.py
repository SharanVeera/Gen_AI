import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# List all models
models = genai.list_models()

for m in models:
    # Only show models that support generateContent
    if "generateContent" in m.supported_generation_methods:
        print(m.name)
