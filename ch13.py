#XML, JSON, API requests (google, twitter)

import xml.etree.ElementTree as ET
import urllib.parse
from urllib.request import urlopen
import json
import pprint
#import twurl [for twitter api usage]

def xmlExamples():
   data = '''
   <person>
     <name>Chuck</name>
     <phone type="intl">+1 734 303 4456</phone>
     <email hide="yes"/>
   </person>'''

   myInput = '''
   <stuff>
   <users>
   <user x="2">
   <id>001</id>
   <name>Chuck</name>
   </user>
   <user x="7">
   <id>009</id>
   <name>Brent</name>
   </user>
   </users>
   </stuff>'''

   #convert string representation into XML tree
   tree = ET.fromstring(data)
   print('Name:',tree.find('name').text)
   print('Attr:',tree.find('email').get('hide'))

   stuff = ET.fromstring(myInput)
   users = stuff.findall('users/user')
   print('User count:', len(users))

   for user in users:
      print('Name:', user.find('name').text)
      print('Id', user.find('id').text)
      print('Attribute', user.get('x'))


def jsonExamples():
   input = '''
   [
      { "id" : "001",
         "x" : "2",
         "name" : "Chuck"
      } ,
      { "id" : "009",
         "x" : "7",
         "name" : "Brent"
      }
   ]'''

   info = json.loads(input)
   print('User count:', len(info))
   for item in info:
      print('Name', item['name'])
      print('Id', item['id'])
      print('Attribute', item['x'])

def googleGeocodeApi():
   serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
   while True:
      address = input('Enter a location: ')
      if len(address) < 1 :
         break
      url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address': address})
      print('Retrieving', url)
      googleResponse = urlopen(url)
      #20160511 - data will be returned as bytes
      #use decode when converting data
      data = googleResponse.read()
      print('Retrieved',len(data),'characters')
      #pprint.pprint(data)

      #perform basic verifications
      try:
         js = json.loads(str(data.decode()))
      except:
         js = None

      if js == None or 'status' not in js or js['status'] != 'OK':
         print('==== Failure To Retrieve ====')
         continue

      print(json.dumps(js, indent=2))

   lat = js["results"][0]["geometry"]["location"]["lat"]
   lng = js["results"][0]["geometry"]["location"]["lng"]

   countryCode = 'No associated country'
   #fetch country code, no direct access, need to loop and check
   for component in js["results"][0]["address_components"]:
      if component['types'][0] == "country":
         countryCode = component["short_name"]

   print('lat',lat,'lng',lng)
   print('Country is:', countryCode)
   location = js['results'][0]['formatted_address']
   print(location)


if __name__ == "__main__":
  #xmlExamples()
  #jsonExamples()
  googleGeocodeApi()