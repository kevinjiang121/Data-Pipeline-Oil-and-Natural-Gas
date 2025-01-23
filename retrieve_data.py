import requests
from dotenv import load_dotenv
import os

def retrieve_data():
    load_dotenv()
    EIA_API_KEY = os.getenv('EIA_API_KEY')
    if not EIA_API_KEY:
        raise ValueError("EIA_API_KEY not found in environment variables.")
    
    route = "https://api.eia.gov/v2/petroleum/cons/wpsup/data"
    params = {
        "api_key": EIA_API_KEY,
        "frequency": "weekly", 
        "start": "2020-01-01",
        "end": "2025-01-01",
        "data[]": "value",
        "offset": 0,
        "length": 5000
    }

    print(f"Requesting data from: {route}")
    print(f"Using parameters: {params}")
    response = requests.get(route, params=params)
    response.raise_for_status()
    data = response.json()

    if not data.get("response", {}).get("data", []):
        print("No data returned.")
    return data