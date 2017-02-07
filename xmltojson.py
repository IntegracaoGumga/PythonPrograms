#importacoes
import json, xmltodict, sys, optparse, xml.etree.cElementTree as ET

# validar numero de parametros
if len(sys.argv) < 6:
    print "Numero de parametro esta incorreto"
    exit(1)

# atribuicao de variaveis
options = optparse.Values({"pretty": False})

pc_ignRootElement = True
pc_changeSeparetorLabel = True
pc_force_list = ''
stringJsonReturn = ''

# atribuicoes dos parametros
for i in range(len(sys.argv)):
    if i == 1:
        pc_xml = sys.argv[i]
    elif i == 2:
        pc_debug = sys.argv[i]
    elif i == 3:
        if sys.argv[i] == '1':
            pc_ignRootElement = True
    elif i == 4:
        pc_changeSeparetorLabel = sys.argv[i]
    elif i == 5:
        pc_force_list = sys.argv[i]

# converte o xml em dict e o dict em json
def convert(pc_xml, xml_attribs=False):
    d = xmltodict.parse(pc_xml,xml_attribs=xml_attribs,force_list=pc_force_list)
    return json.dumps(d,indent=4)

# chama a conversao do xml
stringJson = convert(pc_xml)

# varre o json para remover a tag root
if pc_ignRootElement == True:
   jsonLoads = json.loads(stringJson)
   stringMainKey = jsonLoads.keys()[0]
   stringAux = jsonLoads.__getitem__(stringMainKey)
   newString = json.dumps(stringAux)
   if pc_changeSeparetorLabel == "'":
       stringJsonReturn = newString.replace("\"",pc_changeSeparetorLabel)
   else:
       stringJsonReturn = newString
else:
   if pc_changeSeparetorLabel == "'":
       stringJsonReturn = stringJson.replace("\"",pc_changeSeparetorLabel)
   else:
       stringJsonReturn = stringJson

# retorna o json formatado
print stringJsonReturn
