class Weather:
    def __init__(self, lat=None, lon=None):
        self.params = {
            "latitude": lat,
            "longitude": lon,
            "hourly": ["temperature_2m", "precipitation_probability", "cloud_cover"],
        }

    def get_weather(self) -> dict:
        import requests

        response = requests.get(
            "https://api.open-meteo.com/v1/forecast", params=self.params
        )
        return response
