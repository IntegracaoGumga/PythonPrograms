import sys
from xml2json import json2xml

if len(sys.argv) <= 1:
   sys.exit()

json = sys.argv[-1]
xml = json2xml(json)

print(xml)
