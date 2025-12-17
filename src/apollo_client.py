import os
import requests

APOLLO_API_KEY = os.getenv("APOLLO_API_KEY")

BASE_URL = "https://api.apollo.io/v1"

def search_people(titles=None, locations=None, page=1):
    """
    Search people using Apollo API (conceptual/demo use).
    """
    url = f"{BASE_URL}/mixed_people/search"

    payload = {
        "api_key": APOLLO_API_KEY,
        "person_titles": titles or [],
        "locations": locations or [],
        "page": page
    }

    response = requests.post(url, json=payload)

    if response.status_code != 200:
        raise Exception(f"Apollo API error: {response.text}")

    return response.json()
