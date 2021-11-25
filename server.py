server_struc = {
 "server": [
      { "server": { "ser_id": "S1" ,"ser_name":"server1" , "ip-address": "10.2.3.1","services": 
                   [   
                      {"services": "ssh" , "port": "22", "tcp/udp": "tcp"},
                      {"services": "smtp" , "port": "25", "tcp/udp": "tcp"},
                      {"services": "http" , "port": "80", "tcp/udp": "tcp"} 
                   ]
                 }
      },
     
      { "server": { "ser_id": "S2" ,"ser_name":"server2" , "ip-address": "10.2.3.2","services": 
                   [   
                    {"services": "ipp" , "port": "631", "tcp/udp": "tcp"},
                    {"services": "ppp" , "port": "3000", "tcp/udp": "tcp"},
                    {"services": "http-proxy" , "port": "8080", "tcp/udp": "tcp"} 
                   ]     
                 }
      },
     { "server": { "ser_id": "S3" ,"ser_name":"server3" , "ip-address": "10.2.3.3","services": 
                   [   
                      {"services": "ssh" , "port": "22", "tcp/udp": "tcp"},
                      {"services": "smtp" , "port": "25", "tcp/udp": "tcp"},
                      {"services": "http" , "port": "80", "tcp/udp": "tcp"} 
                   ]
                 }
      },
        ]
}

import yaml
yaml_data = yaml.dump(server_struc)
print(yaml_data)