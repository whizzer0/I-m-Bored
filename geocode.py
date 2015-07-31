import requests
import json

def GeoCode(location, country):
    api = "AIzaSyB2ZNS8iQeVcwGp2gXuRDQOL7GTCpypExk"
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    
    request_parameters = {
        'address': location + ", " + country,
        'key': api
	}
	
    r = requests.get(url, params = request_parameters)
    results = json.loads(r.text)
    
    output = {
        "lat": results['results'][0]['geometry']['location']['lat'],
        "lng": results['results'][0]['geometry']['location']['lng']
    }
    
    return output
