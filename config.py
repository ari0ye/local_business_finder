import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# API Keys
GEOAPIFY_API_KEY = os.getenv("GEOAPIFY_API_KEY")  # Geoapify API key from environment

# API Endpoints
PLACES_BASE_URL = "https://api.geoapify.com/v2/places"  # Endpoint for places search
GEOCODING_URL = "https://api.geoapify.com/v1/geocode/search"  # Endpoint for geocoding

# Defaults
DEFAULT_SEARCH_RADIUS = 5000  # Default search radius in meters
DEFAULT_MAX_RESULTS = 10  # Default maximum number of results
