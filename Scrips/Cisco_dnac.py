#CISCO DNAC SCRIPT
#FILL IN THE MISSING PARTS AND TEST IF THE SCRIPT RUNS

import requests
import json
requests.packages.urllib3.disable_warnings () 
DNAC_user = input("Username? ") #'devnetuser'
DNAC_psw = input("Password? ")  #'Cisco123!'
token_req_url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"
auth = (DNAC_user, DNAC_psw)
req = requests.post(token_req_url, auth=auth, verify=False)
print("API Return Code: " + str(req.status_code))  
print('Request URI: ' + token_req_url)
print("Username: " + DNAC_user)
resp = req.text
print(req.json())
token = req.json()['Token']
print("Received Token:")
print(token)
print("Length Token:")
print(len(token))
