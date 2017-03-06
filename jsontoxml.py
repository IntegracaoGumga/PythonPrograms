import sys, json, dicttoxml

if len(sys.argv) < 1:
    sys.exit()

p_root = 'root'
p_xml = ''

for i in range(len(sys.argv)):
    if i == 1:
        p_json = sys.argv[i]
    if i == 2:
        p_root = sys.argv[i]

try:
    json_data = json.loads(p_json)
    p_xml = dicttoxml.dicttoxml(json_data, custom_root=p_root)
except:
    p_xml = ''

print p_xml
