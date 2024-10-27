import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

zone_id = os.getenv('ZONE_ID')  
api_token = os.getenv('API_TOKEN') 

name = os.getenv('NAME')  
content = os.getenv('CONTENT') 

url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records'

dns_record_data = {
    "comment": name,
    "name": name,
    "proxied": False,
    "settings": {},
    "tags": [],
    "ttl": 0,
    "content": content,
    "type": "A"
}
print(name)

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_token}'
}

response = requests.post(url, headers=headers, json=dns_record_data)

if response.status_code == 200:
    result = response.json()
    
    with open('create_record.json', 'w') as json_file:
        json.dump(result, json_file, indent=4)
    
    print("create_record")
else:
    print(f"Error: {response.status_code} - {response.text}")
