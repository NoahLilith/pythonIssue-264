import requests

def get_public_ip():
    response = requests.get("https://api.ipify.org?format=json")
    ip_data = response.json()
    return ip_data['ip']

def get_geolocation(api_key):
    url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={api_key}"
    payload = {
        "considerIp": "true"
    }
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 403:
        print("Access forbidden: Check your API key and service restrictions.")
        print(response.json())
        return None
    elif response.status_code != 200:
        print(f"Error: {response.status_code}")
        print(response.json())
        return None

    location_data = response.json()
    return location_data['location']

# 你的 Google Geolocation API 密钥
API_KEY = 'AIzaSyBp5glOERo1EPg_9boiCdweZuwp-tEgp1o'

public_ip = get_public_ip()
print(f"Public IP Address: {public_ip}")

location = get_geolocation(API_KEY)
if location:
    latitude = location['lat']
    longitude = location['lng']
    print(f"Latitude: {latitude}, Longitude: {longitude}")
else:
    print("Failed to get location data.")