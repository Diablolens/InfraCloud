import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
iphost = 'sandboxdnac.cisco.com'
interface = 'GigabitEthernet1'
username = 'devnetuser'
password = 'Cisco123!'
#Curl in python

headers = {
    'Accept': 'application/yang-data+json',
}

response = requests.get('https://'+ iphost+ '/restconf/data/ietf-interfaces:interfaces/interface=' + interface, headers=headers, verify=False, auth=('$USERNAME', '$PASSWORD'))

if response.status_code==200:
    print("status ok")
   
else:
    print("status not ok")