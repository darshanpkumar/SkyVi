import requests
from config import USERNAME, PASSWORD

BASE_URL = "https://opensky-network.org/api"

def get_all_flights():
    url = f"{BASE_URL}/states/all"

    try:
        response = requests.get(
            url,
            auth=(USERNAME, PASSWORD),
            timeout = 10
        )
        response.raise_for_status()
        return response.json()
    
    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}")
        return None

import requests
from config import USERNAME, PASSWORD

BASE_URL = "https://opensky-network.org/api"


def get_all_flights():
    """
    Fetch all live flights from the OpenSky Network API.
    """
    url = f"{BASE_URL}/states/all"

    try:
        response = requests.get(
            url,
            auth=(USERNAME, PASSWORD),
            timeout=10
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}")
        return None


def search_flight(callsign):
    """
    Search for a flight by its callsign.
    Example: AI101, EK515, BA256
    """
    data = get_all_flights()

    if not data:
        return None

    callsign = callsign.upper().strip()

    for flight in data.get("states", []):

        # Ensure enough data exists
        if len(flight) < 17:
            continue

        if flight[1] is not None:

            if flight[1].strip().upper() == callsign:

                return {
                    "icao24": flight[0],
                    "callsign": flight[1].strip(),
                    "country": flight[2],
                    "last_position_update": flight[3],
                    "last_contact": flight[4],
                    "longitude": flight[5],
                    "latitude": flight[6],
                    "altitude_ft": round(flight[7] * 3.28084) if flight[7] is not None else None,
                    "on_ground": flight[8],
                    "velocity_kmh": round(flight[9] * 3.6, 2) if flight[9] is not None else None,
                    "heading": flight[10],
                    "vertical_rate": flight[11],
                    "geo_altitude": flight[13],
                    "squawk": flight[14],
                    "spi": flight[15],
                    "position_source": flight[16]
                }

    return None