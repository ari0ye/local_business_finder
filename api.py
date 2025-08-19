import requests
from config import GEOAPIFY_API_KEY

def make_api_request(url, params):
    # Add API key to parameters
    params["apiKey"] = GEOAPIFY_API_KEY
    try:
        # Send GET request to the API
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise error for bad responses
        return response.json()  # Return parsed JSON data
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")  # Print error message
        return None  # Return None on failure
