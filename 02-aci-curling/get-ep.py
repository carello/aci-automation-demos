import requests
import json

# Intent of this script is to login, get a token/cookie and get all the endpoints on the fabric 
# Not very secure being that the credentials are in the script.

#CONTROLLER = "http://enter the APIC IP Address"
#USERNAME = 'enter the user name; probably admin'
#PASSWORD = "Enter your password"


r = requests.post(CONTROLLER + '/api/aaaLogin.json', json={'aaaUser':{"attributes":{'name': USERNAME,'pwd': PASSWORD}}}, verify=False)
r_json = r.json()
token = r_json["imdata"][0]["aaaLogin"]["attributes"]["token"]
cookie = {'APIC-cookie':token}
r_ep = requests.get(CONTROLLER + '/api/node/class/fvCEp.json', cookies=cookie, verify=False)
ep_json = r_ep.json()
print("++++++++++++++++++++++++++++++++++++++++++")
print(json.dumps(ep_json, indent=4, sort_keys=True))

