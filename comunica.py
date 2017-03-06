import sys
import requests
import json
import ast

headers = {'Content-type': 'application/json'}

if len(sys.argv) < 2:
    print "Numero de parametro esta incorreto"
    exit(0)
    
for i in range(len(sys.argv)):
    if i == 1:
        param1_url = sys.argv[i]
    elif i == 2 :
        param2_obj = sys.argv[i]
    elif i == 3:
        param3_action = sys.argv[i]
    elif i == 4:
        param4_id = sys.argv[i]  

if 'param3_action' in locals():
    if param3_action == 'post':
        #INSERT POST
        bodyDumps = json.dumps(param2_obj)
        bodyDumps = bodyDumps.replace("\"","")
        bodyDumps = bodyDumps.replace("\'","\"")
        bodyDumps = bodyDumps.replace("\"True\"","true")
        #bodyDumps = json.dumps(param2_obj) 
        #bodyLoads = json.loads(bodyDumps)
        #print 'bodyDumps', bodyDumps
        r = requests.post(param1_url,data=bodyDumps,headers=headers)
        #print r.json()
        #print r.text
        print r.status_code
    elif param3_action == 'get':
        #GET
        r = requests.get(param1_url)
        json_print = ''
        try:
            json_print = json.dumps(r.json())
        except:
            json_print = ''
        print json_print
        #if str(r.status_code)[:1] == '2':
            #print json.dumps(r.json())
        #else:
            #print 'Retorno invalido'
    elif param3_action == 'delete':
        #DELETE
        r = requests.delete(param1_url)
        print r.status_code
    elif param3_action == 'put':
        #UPDATE
        bodyDumps = json.dumps(param2_obj)
        bodyDumps = bodyDumps.replace("\"","")
        bodyDumps = bodyDumps.replace("\'","\"")
        bodyDumps = bodyDumps.replace("\"True\"","true")
        #print bodyDumps
        r = requests.put(param1_url,data=bodyDumps,headers=headers)
        print r.status_code

#print r.status_code
