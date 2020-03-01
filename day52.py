import requests
url1 = 'https://api.datamuse.com/words'
params = {"rel_rhy":"donut"}
request = requests.get(url1, params=params)
request.status_code
req_json = request.json()
for i in req_json[:5]:
    print(i['word'])
