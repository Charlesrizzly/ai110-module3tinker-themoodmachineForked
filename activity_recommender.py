"""
Activity recommender for the Mood Machine.

Uses Yelp Fusion API to find nearby activities based on the user's
detected mood and the 3-label system (positive, negative_relax, negative_cheerup).
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

YELP_API_KEY = os.getenv("YELP_API_KEY")
YELP_SEARCH_URL = "https://api.yelp.com/v3/businesses/search"

# Maps 3-label mood to search terms for Yelp.
MOOD_TO_QUERY = {
    "positive":          "restaurant",
    "negative_relax":    "yoga",
    "negative_cheerup":  "comedy",
}

# Opening line printed before the activity list.
MOOD_FRAMING = {
    "positive":          "Wonderful! Here's how to keep the good vibes going:",
    "negative_relax":    "Here are some relaxing activities nearby to help you unwind:",
    "negative_cheerup":  "Here are some fun activities nearby to cheer you up:",
}


def get_activities(mood: str, location: str, limit: int = 5) -> list:
    """
    Query Yelp Fusion API for places matching the given mood near location.

    Returns a list of dicts with keys: name, category, address, distance.
    Returns an empty list on any API error.
    """
    if not YELP_API_KEY:
        print("[activity_recommender] No YELP_API_KEY found in .env")
        return []

    query = MOOD_TO_QUERY.get(mood, "activities")
    headers = {
        "Authorization": f"Bearer {YELP_API_KEY}",
        "Accept": "application/json"
    }
    params = {"location": location, "term": query, "limit": limit}

    try:
        resp = requests.get(YELP_SEARCH_URL, headers=headers, params=params, timeout=8)
        resp.raise_for_status()
        data = resp.json()
    except requests.RequestException as e:
        print(f"[Yelp] Error: {e}")
        return []

    results = []
    for business in data.get("businesses", []):
        results.append({
            "name":     business.get("name", "Unknown"),
            "category": (business.get("categories") or [{}])[0].get("title", "Activity"),
            "address":  business.get("location", {}).get("address1", "N/A"),
            "distance": business.get("distance", 0),
        })
    return results


def format_response(mood: str, activities: list) -> str:
    """Build the final string to print to the user."""
    lines = [MOOD_FRAMING.get(mood, "Here are some activities nearby:"), ""]

    if not activities:
        lines.append("  (No results — check your API key and location.)")
        return "\n".join(lines)

    for i, act in enumerate(activities, 1):
        km = act["distance"] / 1000
        lines.append(f"  {i}. {act['name']} ({act['category']})")
        lines.append(f"     {act['address']}  —  {km:.1f} km away")

    return "\n".join(lines)
