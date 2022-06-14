# from netmiko import Netmiko
# connection = Netmiko(host='10.1.1.10', port='22', username='u1', password='cisco', device_type='cisco_ios')

from netmiko import ConnectHandler
# creating a dictionary for the device to connect to
cisco_device = {
       'device_type': 'cisco_ios',     #device type from https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py
       'host': '192.168.59.171',
       'username': 'cisco',
       'password': 'cisco',
       'port': 22,             # optional, default 22
       'secret': 'cisco',      # this is the enable password
       'verbose': True         # optional, default False
       }

# connecting to the device and returning an ssh connection object
connection = ConnectHandler(**cisco_device)
print('Entering the enabel mode....')
connection.enable()
# commands = ['int loopback 0', 'ip address 1.1.1.1 255.255.255.255', 'exit', 'username netmiko secret cisco']
# output = connection.send_config_set(commands)
# cmd = 'ip ssh version 2;access-list 1 permit any;ip domain-name cisco.local'
# output = connection.send_config_set(cmd.split(';'))
cmd = '''ip ssh version 2
access-list 1 permit any
ip domain-name cisco.local
'''
output = connection.send_config_set(cmd.split('\n'))
print(output)
print(connection.find_prompt())

connection.exit_config_mode()
# closing the connection
print('Closing connection')
connection.disconnect()