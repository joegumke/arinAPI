#!/usr/bin/python3

#Dependency -> Maxmind Geo2Country DB . Requires a free account.
#Usage: arinRPI.py $IP 

import maxminddb
import requests, sys, json
import xml.etree.ElementTree as ET

def main(argv):
    ip = sys.argv[1]
    url='http://whois.arin.net/rest/ip/'+ip
    print("Making Request to:" + url)
    response = requests.get(url)
    root = ET.fromstring(response.content)
    for child in root.iter('*'):
        print(child.tag,child.text)

    try:
        reader = maxminddb.open_database('GeoLite2-Country.mmdb')
        country = reader.get(ip)
        result = json.dumps(country, indent=4 ,sort_keys=True)
        print(result)
        
    except Exception:
        print('you dont have Maxmind DB in current Directory. Exiting....')
        exit()
    

if __name__ == "__main__":
    main(sys.argv[1])
