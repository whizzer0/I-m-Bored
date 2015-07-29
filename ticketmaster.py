#1. mock up either side of the api
#- pretend date
#- format in lines to the console

#API KEY uwmnATt30UNVTSdoNAMg1TTemjPG1BzS
import requests
import xml.etree.ElementTree as ET

def lookUpTicketmaster(longitude, latitude, datefrom, dateto, budget):
	#declaring a new variable that holds a date that is formatted to the api's requirements
	#date = "2015072800-2015080100"
	#declaring a new variable that holds the api key above
	api = "uwmnATt30UNVTSdoNAMg1TTemjPG1BzS"
	
	#we need a variable that holds a string containing the location we want to search from (SEE THE DOCUMENTATION ON THE WEBSITE FOR THE FORMAT)
	#location = 'Norwich, United Kingdom'
	#we need a variable that holds a integer page_size that is the maximum number of results to be returned
	#result_number = 54 #no we don't
	#we need a variable that holds the default range in km. much more useful.
	defrange = 50
	base_url = "https://app.ticketmaster.eu/mfxapi/v1/events"
	#define the headers! we want this in json
	headers = {"Accept": "application/json"}
	request_parameters = {
		"app_key": api,
		#"date": date,
		#"location": location,
		#"page_size": result_number
		"radius": defrange,
		"domain_ids": "unitedkingdom",
		"lang": "en-us", #only one it supports :(
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

#for event in root.iter('events'):
#	for node in event:
#		#this is outpi=utting the <title> element
#		print node.tag, node.attrib, node.find('title').text,



#olde legacy code

##self-explanatory
#import requests
#
##set default url. temporary?
#url = "https://app.ticketmaster.eu/mfxapi/v1/events?apikey=uwmnATt30UNVTSdoNAMg1TTemjPG1BzS&domain_ids=unitedkingdom&lang=en-us&lat=52.478655&long=-1.910211&radius=50&eventdate_from=2015-08-01T00:00:00Z&eventdate_to=2015-09-01T00:00:00Z&max_price=500&is_seats_available=true&is_not_cancelled=true&is_not_package=true&sort_by=proximity"
##get user input for variables. temporary.
#if not raw_input("skip 'n' use default? "):
#    latitude = raw_input("wot latitude? ")
#    longitude = raw_input("wot longitude? ")
#    datefrom = raw_input("wot date from? (iso 8601 plz) ")
#    dateto = raw_input("wot date to? (iso 8601 plz) ")
#    maxprice = raw_input("wot cash u got? ")
#    #figure out the url
#    url = "https://app.ticketmaster.eu/mfxapi/v1/events?apikey=uwmnATt30UNVTSdoNAMg1TTemjPG1BzS&domain_ids=unitedkingdom&lang=en-us&lat=" + latitude + "&long=" + longitude + "&radius=50&eventdate_from=" + datefrom + "T00:00:00Z&eventdate_to=" + dateto + "T00:00:00Z&max_price=" + maxprice + "&price_excl_fees=true&is_seats_available=true&is_not_cancelled=true&is_not_package=true&sort_by=proximity"
##add the header
#headers = {'Accept': 'application/json'}
#
##for debugging
#print(url)
##finally GET the data using the stuff we set earlier
#r = requests.get(url, headers=headers)
##convert the json into python dictionaries so that we can use it
#Jason = r.json()
##print stuff for demo purposes
##print(Jason)
#print(Jason[u'events'][1-4][u'name'])
#
##Emergency backup everything's-exploding-help URL for demo
##https://app.ticketmaster.eu/mfxapi/v1/events?apikey=uwmnATt30UNVTSdoNAMg1TTemjPG1BzS&domain_ids=unitedkingdom&lang=en-us&lat=52.478655&long=-1.910211&radius=50&eventdate_from=2015-08-01T00:00:00Z&eventdate_to=2015-09-01T00:00:00Z&max_price=500&is_seats_available=true&is_not_cancelled=true&is_not_package=true&sort_by=proximity
##Note the lat/long of the ICC (YRS FOC WK venue) - 52.478655, -1.910211
