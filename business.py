class Business:
    def __init__(self, name, address, lat, lon, website=None, email=None):
        # Initialize business attributes
        self.name = name
        self.address = address
        self.lat = lat
        self.lon = lon
        self.website = website
        self.email = email

    def __repr__(self):
        # String representation for debugging
        return f"Business(name={self.name}, address={self.address})"

    def to_dict(self):
        # Convert business object to dictionary
        return {
            "name": self.name,
            "address": self.address,
            "lat": self.lat,
            "lon": self.lon,
            "website": self.website,
            "email": self.email
        }
