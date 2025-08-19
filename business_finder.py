from config import PLACES_BASE_URL
from api import make_api_request
from business import Business

def find_businesses(lat, lon, category, limit=10):
    # Prepare API request parameters for Geoapify Places API
    params = {
        "categories": category,
        "filter": f"circle:{lon},{lat},1000",  # Search within 1km radius of (lat, lon)
        "limit": limit
    }
    data = make_api_request(PLACES_BASE_URL, params)  # Make API call and get response

    businesses = []
    if data and "features" in data:
        for place in data["features"]:
            props = place.get("properties", {})
            # Create a Business object from the API response properties
            b = Business(
                name=props.get("name"),
                address=props.get("formatted"),
                lat=place["geometry"]["coordinates"][1],  # Latitude from geometry
                lon=place["geometry"]["coordinates"][0],  # Longitude from geometry
                website=props.get("website"),
                email=props.get("email")
            )
            businesses.append(b)  # Add business to the results list
    return businesses  # Return the list of found businesses
