import requests

# Enter dna center API example -> dna/intent/api/v1/network-device
API = input('Enter the API: ')

# Enter base64 basic auth include Basic before entering key
Authorization = input('Enter the base64 basic authentication: ')

url = 'https://sandboxdnac2.cisco.com/dna/'

headers = {'Authorization': Authorization}


response = requests.request("GET", url, headers=headers)
print (response.text)


# Enter API token recieved from above **DONT FORGET -> ''
token = input('Enter API token recieved: ')

headers = {'X-Auth-Token': token}, {'accept': "application/json"}

# Get Network Devices, client health, etc.. depending on the API entered above.
response = requests.request("GET", url + API, headers=headers)
print (response.text)
