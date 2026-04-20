#!/usr/bin/env python3
"""Quick test to debug the Foursquare API."""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("FOURSQUARE_API_KEY")
print(f"API Key loaded: {API_KEY}")
print(f"API Key length: {len(API_KEY) if API_KEY else 'None'}")

if not API_KEY:
    print("ERROR: No API key found in .env")
    exit(1)

# Test a simple API call
url = "https://api.foursquare.com/v3/places/search"
headers = {"Authorization": API_KEY, "Accept": "application/json"}
params = {"query": "yoga", "near": "Austin TX", "limit": 1}

print("\nTesting API call...")
print(f"URL: {url}")
print(f"Headers: {headers}")
print(f"Params: {params}")

try:
    resp = requests.get(url, headers=headers, params=params, timeout=8)
    print(f"\nStatus Code: {resp.status_code}")
    print(f"Response: {resp.text[:500]}")
except Exception as e:
    print(f"Error: {e}")
