class Coordinates:
    def __init__(self, name=None, latitude=None, longitude=None):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def get_cooords(self, name):
        import requests

        response = requests.get(
            f"https://geocoding-api.open-meteo.com/v1/search?name={name}"
        )
        if response.status_code == 200:
            response = response.json()
            response = response["results"][0]
            coordinates = Coordinates(
                latitude=response.get("latitude"), longitude=response.get("longitude")
            )
            return coordinates
        return None
