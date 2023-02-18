import json

json_data = open("sample-data.json").read()
json_object = json.loads(json_data)

print("""
INTERFACE STATUS
================================================================================
DN                                                 Description           Mtu     Speed
-------------------------------------------------- --------------------  ------  ------""")
imdata = json_object['imdata']
for n in range(0,3):
    for i, k in json_object["imdata"][n]['l1PhysIf']["attributes"].items():
        if i == 'dn':
            print(k, end="                              ")
        if i == "mtu":
            print(k, end="     ")    
        if i == "speed":    
            print(k, end="\n")
