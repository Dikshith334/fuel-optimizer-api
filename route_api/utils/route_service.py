import requests
import polyline   # ✅ add this

API_KEY = "eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6IjExZmUxOTBlZDgyMzQ3M2E4MWQ2NmM1YmE2MjliNTE2IiwiaCI6Im11cm11cjY0In0="

def get_route(start, end):
    url = "https://api.openrouteservice.org/v2/directions/driving-car"

    headers = {
        "Authorization": API_KEY,
        "Content-Type": "application/json"
    }

    body = {
        "coordinates": [start[::-1], end[::-1]]
    }

    response = requests.post(url, json=body, headers=headers).json()

    if "routes" not in response:
        return None

    route = response["routes"][0]

    # ✅ Decode geometry
    decoded_coords = polyline.decode(route["geometry"])

    return {
        "distance_miles": route["summary"]["distance"] / 1609,
        "geometry": route["geometry"],
        "coordinates": decoded_coords   # ✅ now usable
    }