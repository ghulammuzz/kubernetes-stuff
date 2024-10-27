import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

zone_id = os.getenv('ZONE_ID')  
api_token = os.getenv('API_TOKEN')  

url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_token}'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    dns_records = response.json()

    with open('list_record.json', 'w') as json_file:
        json.dump(dns_records, json_file, indent=4)
    
    print("save in list_record.json")
else:
    print(f"Error: {response.status_code} - {response.text}")
