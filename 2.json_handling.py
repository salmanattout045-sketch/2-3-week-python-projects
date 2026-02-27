import json

with open ("states.json") as f:
    json_data = json.load(f)
for state in json_data["states"]:
    del state["area_codes"]
    print(state["name"], state["abbreviation"])

with open ("new_states.json","w") as f:
    json.dump(json_data,f,indent=2)


#2 real world use of it:
import json
from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
    source = response.read()

data = json.loads(source)

# print(json.dumps(data, indent=2))

usd_rates = dict()

for item in data['list']['resources']:
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']
    usd_rates[name] = price

print(50 * float(usd_rates['USD/INR']))


