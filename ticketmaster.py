#self-explanatory
import requests

#set default url. temporary?
url = "https://app.ticketmaster.eu/mfxapi/v1/events?apikey=uwmnATt30UNVTSdoNAMg1TTemjPG1BzS&domain_ids=unitedkingdom&lang=en-us&lat=52.478655&long=-1.910211&radius=50&eventdate_from=2015-08-01T00:00:00Z&eventdate_to=2015-09-01T00:00:00Z&max_price=500&is_seats_available=true&is_not_cancelled=true&is_not_package=true&sort_by=proximity"
#get user input for variables. temporary.
if not raw_input("skip 'n' use default? "):
    latitude = raw_input("wot latitude? ")
    longitude = raw_input("wot longitude? ")
    datefrom = raw_input("wot date from? (iso 8601 plz) ")
    dateto = raw_input("wot date to? (iso 8601 plz) ")
    maxprice = raw_input("wot cash u got? ")
    #figure out the url
    url = "https://app.ticketmaster.eu/mfxapi/v1/events?apikey=uwmnATt30UNVTSdoNAMg1TTemjPG1BzS&domain_ids=unitedkingdom&lang=en-us&lat=" + latitude + "&long=" + longitude + "&radius=50&eventdate_from=" + datefrom + "T00:00:00Z&eventdate_to=" + dateto + "T00:00:00Z&max_price=" + maxprice + "&price_excl_fees=true&is_seats_available=true&is_not_cancelled=true&is_not_package=true&sort_by=proximity"
#add the header
headers = {'Accept': 'application/json'}

#for debugging
print(url)
#finally GET the data using the stuff we set earlier
r = requests.get(url, headers=headers)
#convert the json into python dictionaries so that we can use it
Jason = r.json()
#print stuff for demo purposes
#print(Jason)
print(Jason[u'events'][1-4][u'name'])

#Emergency backup everything's-exploding-help URL for demo
#https://app.ticketmaster.eu/mfxapi/v1/events?apikey=uwmnATt30UNVTSdoNAMg1TTemjPG1BzS&domain_ids=unitedkingdom&lang=en-us&lat=52.478655&long=-1.910211&radius=50&eventdate_from=2015-08-01T00:00:00Z&eventdate_to=2015-09-01T00:00:00Z&max_price=500&is_seats_available=true&is_not_cancelled=true&is_not_package=true&sort_by=proximity
#Note the lat/long of the ICC (YRS FOC WK venue) - 52.478655, -1.910211
