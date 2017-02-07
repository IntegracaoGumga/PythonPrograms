import json, xmltodict, sys

if len(sys.argv) <> 2:
    print "Numero de parametro esta incorreto"
    exit(1)

for i in range(len(sys.argv)):
    if i == 1:
        pc_xml = sys.argv[i]
    elif i == 2:
        pc_force_list = sys.argv[i]

def convert(pc_xml, pc_force_list, xml_attribs=False):
    with open(pc_xml, "rb") as f:
        d = xmltodict.parse(f,xml_attribs=xml_attribs,force_list=pc_force_list)

    return json.dumps(d, indent=4)

print convert(pc_xml, pc_force_list)