rack_struc = {
 "rack": [
      { "device": { "dev_id": "D1" ,"dev_name":"R1" , "role": "router","interfaces": 
                   [   
                      {"interface": "GigabitEhternet1" , "ipaddress": "10.0.1.1", "subnet_mask": "255.255.255.0"},
                      {"interface": "GigabitEhternet2" , "ipaddress": "10.0.3.1", "subnet_mask": "255.255.255.0"},
                      {"interface": "GigabitEhternet3" , "ipaddress": "10.0.4.1", "subnet_mask": "255.255.255.0"} 
                   ]
                 }
      },
     
      { "device": { "dev_id": "D2" , "dev_name": "C1" , "role": "core","interfaces": 
                   [   
                     {"interface": "VLAN1"  ,"ipaddress": "10.0.1.2" , "subnet_mask": "255.255.255.0"}, 
                     {"interface": "VLAN2"  ,"ipaddress": "10.0.2.1" , "subnet_mask": "255.255.255.0"}, 
                     {"interface": "VLAN20" ,"ipaddress": "10.0.20.1", "subnet_mask": "255.255.255.0"} 
                   ]     
                 }
      },
     
      { "device": { "dev_id": "D3" , "dev_name": "AC" , "role": "access","interfaces": 
                   [   
                     {"interface": "VLAN2" ,"ipaddress": "10.0.2.2", "subnet_mask": "255.255.255.0"}
                   ] 
                 }
      }
   ]
}

# !pip install dicttoxml
from dicttoxml import dicttoxml
xml_data = dicttoxml(rack_struc)
print(xml_data)

import json
print('------1---------')
print(type(rack_struc))
print(rack_struc)
#print('------1A--------')
js_struc = json.dumps(rack_struc)
print(type(js_struc))
print(js_struc)
print(json.dumps(rack_struc, indent=8))

print('------1B--------')
g = rack_struc["rack"][0]
print(type(g))
print(g["device"].keys())

print('------2---------')
for g in rack_struc["rack"]:
    print('------2A--------')
    print(type(g))
    print(g)
    print(g["device"]["dev_name"])
    for p in g["device"]["interfaces"]:
        print(p["ipaddress"])
            
print('------3---------')
print("Keys device")
print(g["device"].keys())
print('------3A---------')
print("Keys interfaces")
print(g["device"]["interfaces"][0].keys())

print('------------------ALL-DEVICES-INTERFACES-IP-ADDRESSES------------------')
for connections in rack_struc["rack"]:
    print(connections["device"]["dev_name"])
    for ipadress in connections["device"]["interfaces"]:
        print(ipadress["interface"]+" => "+ipadress["ipaddress"])