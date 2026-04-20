#!/usr/bin/env python3
"""Debug Yelp API connection."""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

YELP_API_KEY = os.getenv("YELP_API_KEY")
print(f"YELP_API_KEY from .env: '{YELP_API_KEY}'")
print(f"Key length: {len(YELP_API_KEY) if YELP_API_KEY else 'None'}")
print(f"Key starts with: {YELP_API_KEY[:20] if YELP_API_KEY else 'None'}")

if not YELP_API_KEY:
    print("ERROR: No YELP_API_KEY found")
    exit(1)

# Test the API call
url = "https://api.yelp.com/v3/businesses/search"
headers = {
    "Authorization": f"Bearer {YELP_API_KEY}",
    "Accept": "application/json"
}
params = {"location": "Austin TX", "term": "yoga", "limit": 1}

print("\nHeaders:")
print(f"  Authorization: Bearer {YELP_API_KEY[:30]}...")
print(f"\nParams: {params}")

try:
    resp = requests.get(url, headers=headers, params=params, timeout=8)
    print(f"\nStatus Code: {resp.status_code}")
    print(f"Response: {resp.text}")
except Exception as e:
    print(f"Error: {e}")
