import requests, os

def get_weather():
    API_KEY = os.getenv("WEATHER_API_KEY", "demo")
    CITY = os.getenv("CITY", "Bengaluru")
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(URL).json()
        return {
            "city": CITY,
            "temp": response["main"]["temp"],
            "description": response["weather"][0]["description"]
        }
    except Exception:
        return {"error": "Failed to fetch weather data"}
