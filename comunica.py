import sys
import requests
import json
import ast

if len(sys.argv) < 4:
    print "Numero de parametro esta incorreto"
    exit(0)

for i in range(len(sys.argv)):
    if i == 1:
        #print sys.argv[i]
        param1_url = sys.argv[i]
    elif i == 2 :
        #print sys.argv[i]
        param2_obj = sys.argv[i]
    elif i == 3:
        #print sys.argv[i]
        param3_action = sys.argv[i]

if 'param3_action' in locals():
    if param3_action == 'post':
        headers = {'Content-type': 'application/json'}
        #INSERT POST
        bodyDumps = json.dumps(param2_obj)
        bodyDumps = bodyDumps.replace("\"","")
        bodyDumps = bodyDumps.replace("\'","\"")
        bodyDumps = bodyDumps.replace("\"True\"","true")
        #bodyDumps = json.dumps(param2_obj) 
        #bodyLoads = json.loads(bodyDumps)
        #print 'bodyDumps', bodyDumps
        r = requests.put(param1_url,data=bodyDumps,headers=headers)
        print r.status_code
    elif param3_action == 'get':
        #GET
        r = requests.get(param1_url)
        print r.status_code
    elif param3_action == 'delete':
        #DELETE
        r = requests.delete(param1_url)
        print r.status_code
#print r.text
