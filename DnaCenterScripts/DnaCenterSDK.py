#! /usr/bin/env python

from dnacantersdk import api

username = input('Enter your username here: ')
password = getpass()
base_url = input('Enter the base url: ')

# Create a DnaCenterAPI connection object

# it uses DNA Center sandbox URL, username and password
DNAC = api.DNACenterAPI(username=username, password=password, base_url=base_url)

# Find all devices
 Devices = DNAC.devices.get_device_list()

# Print formatted select info about the retrieved devices
print ('{0:25s}{1:1}{2:45s}{3:1}{4:15s}'.format("Device Name" "|", \ "Device Type", "|", "Up Time"))
print ('-'*95)
for DEVICE in DEVICES.response:
    print('{0:25s}{1:1}{2:45s}{3:1}{4:15s}'.format(DEVICE.hostname, \ "|", DEVICE.type, "|", DEVICE.uptime))
print ('-'*95)

# Get the health of all clients on during the specific UNIX timestamp
CLIENTS = DNAC.clients.get_overall_client_health(timestamp="Enter UNIX time here")

# Print formatted select info about the retrieved client health stats
print ('{0:25s}{1:1}{2:45s}[3:1}{4:15s}'.format("Client Category", "|",\ "Number of Clients", "|", "Clients Score"))
print ('-'*95)
for CLIENT in CLIENTS.response:
    for score in CLIENT.scoreDetail:
        print ('{0:25s}{1:1}{2:<45d}{3:1}{4:15d}'.format(score.scoreCategory.value, "|", score.clientCount, "|", \ score.scoreValue))
print ('-'*95)


