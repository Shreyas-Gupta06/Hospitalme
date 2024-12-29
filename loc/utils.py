# # loc/utils.py
# import requests
# from django.conf import settings

# def get_hospitals(lat=28.6139, lng=77.2090, radius=15000):
#     api_key = settings.GOOGLE_MAPS_API_KEY
#     url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius={radius}&type=hospital&key={api_key}'
    
#     response = requests.get(url)
#     hospitals_data = response.json()
    
#     return hospitals_data.get('results', [])

import requests
from django.conf import settings
import time

# def get_hospitals(lat=None, lng=None, radius=10000):
#     if not lat or not lng:
#         return []

#     api_key = settings.GOOGLE_MAPS_API_KEY
#     url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius={radius}&type=hospital&key={api_key}'
    
#     hospitals = []
#     while True:
#         response = requests.get(url)
#         hospitals_data = response.json()
#         hospitals.extend(hospitals_data.get('results', []))
        
#         # Check if there's a next page of results
#         next_page_token = hospitals_data.get('next_page_token')
#         if not next_page_token:
#             break
        
#         # Pause to allow the next page token to become available
#         time.sleep(2)  # Google's API documentation suggests a short pause
#         url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?pagetoken={next_page_token}&key={api_key}'
    
#     return hospitals



def get_hospitals(lat, lng, radius=10000):
    api_key = settings.GOOGLE_MAPS_API_KEY
    url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius={radius}&type=hospital&key={api_key}'

    hospitals = []
    while True:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Error: API response status code {response.status_code}")
            break
        hospitals_data = response.json()
        hospitals.extend(hospitals_data.get('results', []))
        
        # Check if there's a next page of results
        next_page_token = hospitals_data.get('next_page_token')
        if not next_page_token:
            break
        
        # Pause to allow the next page token to become available
        time.sleep(2)  # Google's API documentation suggests a short pause
        url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?pagetoken={next_page_token}&key={api_key}'

    return hospitals
