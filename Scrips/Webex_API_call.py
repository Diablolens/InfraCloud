import requests
import json
current_access_token = "Njg4NjY4MjYtN2Q4NC00NzA5LWIyOWQtMTc5OWUyMzA1NTRlYWQ0YWVjZjUtMWFl_P0A1_ffe50b97-2b4a-4965-8373-9822eafeddfd"
uri_scheme = 'https://'
uri_authority_server = 'api.ciscospark.com'
uri_api_path = '/v1/people/me'
url = uri_scheme + uri_authority_server + uri_api_path 
headers = {
    'Authorization': 'Bearer {}'.format(current_access_token),
    'Content-Type': 'application/json'
}
res = requests.get(url, headers=headers)
if res.status_code == 200:
    user_name = res.json()['displayName']
    print("Status is OK")
    print("Username: " + user_name)
else:
    print("Status is not OK")
