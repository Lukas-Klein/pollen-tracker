import dwdpollen
import json
api = dwdpollen.DwdPollenApi()
request = api.get_pollen(120, 124)
requestjson = json.dumps(request, indent=4, sort_keys=True, default=str)

with open('pollenload.json' ,'w') as outfile:
    outfile.write(requestjson)