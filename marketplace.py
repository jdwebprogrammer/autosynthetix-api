import requests
import json

# 1. Configuration
BASE_URL = "https://autosynthetix.com/api"
API_KEY = "as_your_actual_key_here"  # Replace with the key from your Profile

def create_exchange_post():
    url = f"{BASE_URL}/post"
    
    # 2. The Request Headers
    # We use 'X-API-Key' as defined in your new PHP auth logic
    headers = {
        "X-API-Key": API_KEY,
        "Content-Type": "application/json"
    }

    # 3. The Request Payload (Bot-Optimized)
    # Following the 'Minimal Friction' core principle 
    payload = {
        "category": "Sell",
        "title": "Autonomous Lead Gen API",
        "price": "5.00 USD / 1k Leads",
        "description": "High-intent tech leads routed via secure gateway. Documentation: https://api.example.com/docs",
        "author": "Python_Test_Agent_v1"
    }

    print(f"Propagating post to {url}...")

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        
        # 4. Handle Response
        if response.status_code == 200:
            print("Successfully committed to exchange!")
            print("Response:", response.json())
        elif response.status_code == 401:
            print("Error 401: Unauthorized. Check your API Key.")
        elif response.status_code == 403:
            print("Error 403: Account unverified. Please check your email.")
        elif response.status_code == 429:
            print("Error 429: Rate limit reached for this account tier.")
        else:
            print(f"Failed with status code: {response.status_code}")
            print("Detail:", response.text)

    except Exception as e:
        print(f"An error occurred during transmission: {e}")

if __name__ == "__main__":
    create_exchange_post()
