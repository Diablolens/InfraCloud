#CISCO TOKEN SCRIPT
#FILL IN THE MISSING PARTS AND TEST IF THE SCRIPT RUNS
import json

atk = {
    "access_token":"ZDI3MGEyYzQtNmFlNS00NDNhLWFlNzAtZGVjNjE0MGU1OGZmZWNmZDEwN2ItYTU3",
    "expires_in":1209600, 
    "refresh_token":"MDEyMzQ1NjcNTY3ODkwMTIzNDU2NzgDEy1Njc4TEyMzQ1Njc4", 
    "refreshtokenexpires_in":7776000
}

print('============================================ 1 ============================================')
print(json.dumps(atk, indent=8))

print('============================================ 2 ============================================')
print(atk["access_token"])
