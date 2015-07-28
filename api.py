#1. mock up either side of the api
#- pretend date
#- format in lines to the console

#API KEY qgdXKCNgnfsLPLJ7
import requests
import xml.etree.ElementTree as ET

def lookUpEventFul(location):
	#declaring a new variable that holds a date that is formatted to the api's requirements
	date = '2015072800-2015080100'
	#declaring a new variable that holds the api key above
	api = 'qgdXKCNgnfsLPLJ7'
	
	#we need a variable that holds a string containting the location we want to search from (SEE THE DOCUMENTATION ON THE WEBSITE FOR THE FORMAT)
	#location = 'Norwich, United Kingdom'
	#we need a variable that holds a integer page_size that is the maximum number of results to be returned
	result_number = 54
	base_url = 'http://api.eventful.com/rest/events/search'
	request_parameters = {
		'app_key': api,
		'date': date,
		'location': location,
		'page_size': result_number 
	}
	r = requests.get(base_url,params = request_parameters)

	#the following line may strip non-ASCII characters (for XML parser compatibility) and hence may be the cause of some problems with missing characters
	response = r.text.encode('ascii', 'ignore')
	root = ET.fromstring(response)

	return root


'''
<title>Guildhall Tours</title>
<url>http://eventful.com/norwich/events/guildhall-tours-/E0-001-083428214-5@2015073110?utm_source=apis&amp;utm_medium=apim&amp;utm_campaign=apic</url>
<description> &lt;p&gt;Discover the unique history of The Guildhall, England&amp;#39;s largest and most elaborate provincial medieval city hall/description>
<start_time>2015-07-31 10:00:00</start_time>
<stop_time>2015-07-31 11:00:00</stop_time>
<tz_id/>
<tz_olson_path/>
<tz_country/>
<tz_city/>
<olson_path>Europe/London</olson_path>
<venue_id>V0-001-006677700-0</venue_id>
<venue_url>http://eventful.com/norwich/venues/the-guildhall-norwich-/V0-001-006677700-0?utm_source=apis&amp;utm_medium=apim&amp;utm_campaign=apic</venue_url>
<venue_name>The Guildhall - Norwich</venue_name>
<venue_display>1</venue_display>
<venue_address>Gaol Hill</venue_address>
<city_name>Norwich</city_name>
<region_name>Norfolk</region_name>
<region_abbr>NFK</region_abbr>
<postal_code>NR2 1NF</postal_code>
<country_name>United Kingdom</country_name>
<country_abbr2>GB</country_abbr2>
<country_abbr>GBR</country_abbr>
<latitude>52.62905291615308</latitude>
<longitude>1.292143114611008</longitude>
<geocode_type>EVDB Geocoder</geocode_type>
<all_day>0</all_day>
<recur_string>on various days</recur_string>
<calendar_count/>
<comment_count/>
<link_count/>
<going_count/>
<watching_count/>
<created>2015-04-28 08:49:40</created>
<owner>evdb</owner>
<modified>2015-05-04 00:04:20</modified>
<performers/>
<image>
  <url>http://s1.evcdn.com/images/small/I0-001/019/364/096-7.jpeg_/guildhall-tours-96.jpeg</url>
  <width>48</width>
  <height>48</height>
  <caption/>
  <thumb>
    <url>http://s1.evcdn.com/images/thumb/I0-001/019/364/096-7.jpeg_/guildhall-tours-96.jpeg</url>
    <width>48</width>
    <height>48</height>
  </thumb>
  <small>
    <url>http://s1.evcdn.com/images/small/I0-001/019/364/096-7.jpeg_/guildhall-tours-96.jpeg</url>
    <width>48</width>
    <height>48</height>
  </small>
  <medium>
    <url>http://s1.evcdn.com/images/medium/I0-001/019/364/096-7.jpeg_/guildhall-tours-96.jpeg</url>
    <width>128</width>
    <height>128</height>
  </medium>
</image>
<privacy>1</privacy>
<calendars/>
<groups/>
'''

#for event in root.iter('events'):
#	for node in event:
#		#this is outpi=utting the <title> element
#		print node.tag, node.attrib, node.find('title').text, 