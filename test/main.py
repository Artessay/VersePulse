import requests
import json
import os

url = "https://api.langsearch.com/v1/web-search"

payload = json.dumps({
  "query": "tell me the highlights from Apple's 2024 ESG report",
  "freshness": "noLimit",
  "summary": True,
  "count": 10
})
headers = {
  'Authorization': f'Bearer {os.getenv("LANG_SEARCH_API_KEY")}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
