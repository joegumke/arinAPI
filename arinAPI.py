#!/usr/bin/python3

import requests, sys
import xml.etree.ElementTree as ET

def main(argv):
    ip = sys.argv[1]
    url='http://whois.arin.net/rest/ip/'+ip
    print("Making Request to:" + url)
    response = requests.get(url)
    root = ET.fromstring(response.content)
    for child in root.iter('*'):
        print(child.tag,child.text)


if __name__ == "__main__":
    main(sys.argv[1])
