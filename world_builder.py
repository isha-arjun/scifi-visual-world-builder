# 1. Install the official Google GenAI library
!pip install google-genai --quiet

import json
from google import genai
from google.genai import types

# 2. Connect to the Gemini AI Brain
# Put your secret API key inside the quotes below
API_KEY = 'YOUR_GEMINI_API_KEY_HERE'
client = genai.Client(api_key=API_KEY)

# 3. Define the inputs for your Sci-Fi World
planet_name = "Aethelgard"
climate_type = "Bioluminescent Volcanic Jungle"
dominant_faction = "The Iron Guild (Cybernetic Miners)"

# 4. Craft the prompt instructing the AI how to think
prompt = f"""
You are an expert sci-fi world-builder and author. 
Create an immersive, atmospheric lore profile for a fictional planet based on these details:
- Planet Name: {planet_name}
- Climate/Environment: {climate_type}
- Dominant Faction/Inhabitants: {dominant_faction}

Provide the response structured with the following headings:
# 🪐 PLANET PROFILE: {planet_name}
## 🌍 Environment & Ecosystem
## 🤖 The Faction: {dominant_faction}
## 📜 Historical Lore & Secrets
"""

print(f"🚀 Generating world profile for {planet_name}... Please wait...")

# 5. Send the request to Gemini (Updated to the recommended model)
response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=prompt,
)

# 6. Print the beautiful creative output
print("\n" + "="*50 + "\n")
print(response.text)
print("\n" + "="*50)
