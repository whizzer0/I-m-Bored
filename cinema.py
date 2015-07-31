#1. mock up either side of the api
#- pretend date
#- format in lines to the console

#API KEY uwmnATt30UNVTSdoNAMg1TTemjPG1BzS
import requests
#import xml.etree.ElementTree as ET

def lookUpCinema(postcode,justCinemas):
    #postcode = the user's postcode, justCinema = whether to report nearby cinemas (True) or their listings (False)
    #first part - find the nearby cinemas
    url = "http://moviesapi.herokuapp.com/cinemas/find/" + postcode
    ro = requests.get(url)
    pyro = ro.json()
    full = {}
    #print(pyro) #debugging
    #print(pyro[0][u"venue_id"]) #more debugging
    
    #second part - find the actual listings at those cinemas
    if not justCinemas:
        for i in pyro:
            print pyro
            print i
            url = "http://moviesapi.herokuapp.com/cinemas/" + i[u"venue_id"] + "/showings"
            r = requests.get(url)
            pyr = r.json()
            full[i] = pyr
            #print(url) #debuggin'
            #print("") #debugging...
            #print(pyr) #everything's debugging...
            i = i + 1
            return full
    else:
        return pyro

    #the following line may strip non-ASCII characters (for XML parser compatibility) and hence may be the cause of some problems with missing characters
    #response = r.text.encode('ascii', 'ignore')
    #root = ET.fromstring(response)
