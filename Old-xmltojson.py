
from lxml import objectify

def xml_to_dict_recursion(xml_object):
    dict_object = xml_object.__dict__
    if not dict_object:
        return xml_object
    for key, value in dict_object.items():
        dict_object[key] = xml_to_dict_recursion(value)
    return dict_object

def xml_to_dict(xml_str):
    return xml_to_dict_recursion(objectify.fromstring(xml_str))

xml_string = """<?xml version="1.0" encoding="UTF-8"?><Response><NewOrderResp>
<IndustryType>Test</IndustryType><SomeData><SomeNestedData1>a1234</SomeNestedData1>
<SomeNestedData2>3455</SomeNestedData2></SomeData></NewOrderResp></Response>"""

print xml_to_dict(xml_string)

'''
#import xml2json
import xmltodict
import optparse
import sys
import json
import xml.etree.cElementTree as ET

options = optparse.Values({"pretty": False})

if len(sys.argv) < 3:
    print "Numero de parametro esta incorreto"
    exit(1)

ignRootElement = True
changeSeparetorLabel = True

for i in range(len(sys.argv)):
    if i == 1:
        #print sys.argv[i]
        param1 = sys.argv[i]
    elif i == 2:
        #print sys.argv[i]
        param2 = sys.argv[i]
    elif i == 3:
        #print sys.argv[i]
        param3 = sys.argv[i]

stringJsonReturn = ""

#IgnoraRootElement
if 'param2' in locals():
    if param2 == '1':
        ignRootElement = True

#separatorLabel
if 'param3' in locals():
    changeSeparetorLabel = True

try:
    dict = xmltodict.parse(param1)
except ET.ParseError as errorConvert:
    print 'Erro ao tentar converter xml para dict'
    print errorConvert.message
    exit(1)

stringJsonReturn = json.dumps(dict)

try:
    stringJson = xml2json.xml2json(param1, options)
except ET.ParseError as errorConvert:
    print 'Erro ao tentar converter xml para json, verifique se o xml esta com a syntaxe correta!'
    print errorConvert.message
    exit(1)

if ignRootElement == True:
   jsonLoads = json.loads(stringJson)
   stringMainKey = jsonLoads.keys()[0]
   stringAux = jsonLoads.__getitem__(stringMainKey)
   newString = json.dumps(stringAux)
   if changeSeparetorLabel:
       stringJsonReturn = newString.replace("\"",param3)
   else:
       stringJsonReturn = newString
else:
   if changeSeparetorLabel:
       stringJsonReturn = stringJson.replace("\"",param3)
   else:
       stringJsonReturn = stringJson


print stringJsonReturn
'''