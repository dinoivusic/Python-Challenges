import requests

#OPEN NOTIFY API, A simple API serving NASA’s awesome data.
url = 'http://api.open-notify.org'
res = requests.get(url)
print(res.status_code)
people = requests.get('http://api.open-notify.org/astros.json')
ppl = people.json()
print(ppl)

print('The number of people in the space is:', ppl['number'])
for people in ppl['people']:
    print(people['name'])
