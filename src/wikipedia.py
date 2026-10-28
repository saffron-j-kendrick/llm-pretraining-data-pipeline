## IMPORTS

import requests

url = "https://en.wikipedia.org/wiki/Main_Page"

headers = {
    "User-Agent": "Mozilla/5.0"
}

page = requests.get(url, headers= headers)

print(page.status_code)
print(page.content)