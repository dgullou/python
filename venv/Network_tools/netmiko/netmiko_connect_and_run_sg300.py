# from netmiko import Netmiko
# from netmiko.cisco import CiscoS300SSH, CiscoS300Telnet
# connection = Netmiko(host='10.1.1.10', port='22', username='u1', password='cisco', device_type='cisco_ios')

from netmiko import ConnectHandler
# creating a dictionary for the device to connect to
cisco_device = {
       #'device_type': 'cisco_ios',     #device type from https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py
       'device_type': 'cisco_s300',
       'host': '192.168.97.252',
       'username': 'cisco',
       'password': 'Softjack1',
       'port': 22,             # optional, default 22
       #'secret': 'cisco',      # this is the enable password
       'verbose': True         # optional, default False
       }

# connecting to the device and returning an ssh connection object
connection = ConnectHandler(**cisco_device)
prompt = connection.find_prompt()
print(prompt)
connection.enable()
# sending a command and getting the output
output = connection.send_command('sh run')
print(output)

# closing the connection
print('Closing connection')
connection.disconnect()