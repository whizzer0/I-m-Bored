#1. mock up either side of the api
#- pretend date
#- format in lines to the console

#API KEY uwmnATt30UNVTSdoNAMg1TTemjPG1BzS
import requests
import xml.etree.ElementTree as ET
from geocode import GeoCode

def lookUpTicketmaster(location, datefrom, dateto, budget):
	#declare constants that hold important stuffs
	api = "uwmnATt30UNVTSdoNAMg1TTemjPG1BzS"
	base_url = "https://app.ticketmaster.eu/mfxapi/v1/events"
	headers = {"Accept": "application/json"}

	#resolve the lat/long from the location. our app only supports the UK, so country is unnecessary
        geocoded = GeoCode(location, "UnitedKingdom")
        latitude = geocoded["lat"]
        longitude = geocoded["lng"]
	
	request_parameters = {
		"app_key": api,
		"radius": defrange,
		"domain_ids": "unitedkingdom",
		"lang": "en-us",
		"latitude": latitude,
		"longitude": longitude,
		"eventdate_from": datefrom + "T00:00:00Z",
		"eventdate_to": dateto + "T00:00:00Z",
		"max_price": budget,
		"is_seats_available": "true",
		"is_not_cancelled": "true",
		"is_not_package": "true",
		"sort_by": "proximity",
	}
	r = requests.get(base_url,params=request_parameters,headers=headers)
	pyr = r.json()

	#the following line may strip non-ASCII characters (for XML parser compatibility) and hence may be the cause of some problems with missing characters
	response = r.text.encode('ascii', 'ignore')
	root = ET.fromstring(response)

	return root
