import os
import requests
from dotenv import load_dotenv

load_dotenv()

def list_available_models():
    """Check what models are available on OpenRouter"""
    api_key = os.getenv("OPENROUTER_API_KEY")
    
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    
    response = requests.get("https://openrouter.ai/api/v1/models", headers=headers)
    
    if response.status_code == 200:
        models = response.json()['data']
        print("✅ Available models on OpenRouter:")
        for model in models[:10]:  # Show first 10
            print(f"  - {model['id']}")
    else:
        print(f"❌ Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    list_available_models()