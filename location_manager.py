from config import GEOCODING_URL
from api import make_api_request

def get_coordinates(address):
    # Prepare parameters for geocoding API
    params = {"text": address}
    data = make_api_request(GEOCODING_URL, params)  # Make API call

    # Extract coordinates from API response if available
    if data and "features" in data and data["features"]:
        coords = data["features"][0]["geometry"]["coordinates"]
        return coords[1], coords[0]  # Return as (lat, lon)
    return None, None  # Return None if not found
