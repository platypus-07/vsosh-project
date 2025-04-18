import requests

url = 'https://raw.githubusercontent.com/dannyroemhild/ransomware-fileext-list/refs/heads/master/fileextlist.txt'
r = requests.get(url, allow_redirects=True)

open('fileextlist.txt', 'wb').write(r.content)
