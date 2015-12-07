

from urllib2 import urlopen
from json import load
import geonames


def lat_long(location):
    address=location
    #rebuild gooogle api base
    apiUrl = "http://maps.googleapis.com/maps/api/geocode/json?address="+address+"&sensor=false"
    
    #open the apiUrl and assign data to variable
    response = urlopen(apiUrl)
    
    json_obj = load(response)
    
    raw_latlon = json_obj['results'][0]['geometry']['location']
    lat = raw_latlon['lat']
    lon = raw_latlon['lng']
    return (lat, lon)
    
#convert lat/long to timezone
def geo_to_timezone(coordinates):
    lat = coordinates[0]
    lon = coordinates[1]

    geonames_client = geonames.GeonamesClient('demo')
    geonames_result = geonames_client.find_timezone({'lat': lat, 'lng': lon})
    print geonames_result['timezoneId']
    
print lat_long('Mumbai')
print lat_long("Dushanbe")
print lat_long("boston")
print lat_long('san%francisco') #this api link can't have any spaces,replace spaces with '%'
coordinates = lat_long("Mumbai")
geo_to_timezone(coordinates)
