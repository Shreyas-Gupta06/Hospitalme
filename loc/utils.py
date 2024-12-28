# loc/utils.py
import requests
from django.conf import settings

def get_hospitals(lat=17.4933, lng=78.3277, radius=10000):
    api_key = settings.GOOGLE_MAPS_API_KEY
    url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius={radius}&type=hospital&key={api_key}'
    
    response = requests.get(url)
    hospitals_data = response.json()
    
    return hospitals_data.get('results', [])
