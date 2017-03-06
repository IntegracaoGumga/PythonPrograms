#importacoes
import json, xmltodict, sys, optparse, xml.etree.cElementTree as ET, re

# validar numero de parametros
if len(sys.argv) < 4:
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
        if sys.argv[i][:5] == 'file=':
            nome_arquivo = sys.argv[i][5:]
            arq = open(nome_arquivo, 'r')
            pc_xml = arq.read()
            arq.close()
            pc_xml = pc_xml.replace('!ISO8859-1!', '')
        else:
            pc_xml = sys.argv[i]
    elif i == 2:
        if sys.argv[i] == '1':
            pc_ignRootElement = True
    elif i == 3:
        pc_changeSeparetorLabel = sys.argv[i]
    elif i == 4:
        pc_force_list = sys.argv[i]


def postprocessor(path, key, value):
    #if value == None:
    #   return
    if key.count('-INT') > 0:
        try:
            key = key.replace('-INT', '')
            return key, int(value)
        except (ValueError, TypeError):
            return key, value
    elif key.count('-FLOAT') > 0:
        try:
            key = key.replace('-FLOAT', '')
            return key, float(value)
        except (ValueError, TypeError):
            return key, value
    elif key.count('-BOOL') > 0:
        try:
            key = key.replace('-BOOL', '')
            if str(value).lower() == 'true':
               return key, True
            elif str(value).lower() == 'false':
               return key, False
        except (ValueError, TypeError):
            return key, value
    else:
        if key.count('-NN') > 0:
            key = key.replace('-NN', '')
            if value == None:
                value = ""
        elif value == None:
            return
        return key, value

# converte o xml em dict e o dict em json
def convert(pc_xml, xml_attribs=False):
    d = xmltodict.parse(pc_xml,xml_attribs=xml_attribs,postprocessor=postprocessor,force_list=pc_force_list)
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
tamLinha = 30000
x = 0

while x <= len(stringJsonReturn):
    print stringJsonReturn[x: x + tamLinha]
    x = x + tamLinha

#print stringJsonReturn
