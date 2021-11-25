import yaml
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


yaml_data = yaml.dump(rack_struc)
print(yaml_data)

