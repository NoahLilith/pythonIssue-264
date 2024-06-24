import requests
from scapy.all import sniff, ARP

def get_wifi_access_points():
    ap_list = []

    def packet_handler(packet):
        if packet.haslayer(ARP):
            bssid = packet[ARP].hwsrc
            if bssid not in ap_list:
                ap_list.append(bssid)

    sniff(prn=packet_handler, iface='Wi-Fi', timeout=10)

    wifi_access_points = [{"macAddress": ap, "signalStrength": -50} for ap in ap_list]
    return wifi_access_points

def get_geolocation(api_key, wifi_access_points):
    url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={api_key}"
    payload = {
        "wifiAccessPoints": wifi_access_points
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

wifi_access_points = get_wifi_access_points()
print(f"Detected WiFi Access Points: {wifi_access_points}")

location = get_geolocation(API_KEY, wifi_access_points)
if location:
    latitude = location['lat']
    longitude = location['lng']
    print(f"Latitude: {latitude}, Longitude: {longitude}")
else:
    print("Failed to get location data.")