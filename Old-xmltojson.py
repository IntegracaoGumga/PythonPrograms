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

'''
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
'''

print stringJsonReturn