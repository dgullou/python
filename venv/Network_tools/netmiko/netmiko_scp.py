
from netmiko import ConnectHandler
from netmiko import file_transfer
cisco_device = {
       'device_type': 'cisco_ios',     #device type from https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py
       'host': '192.168.59.171',
       'username': 'cisco',
       'password': 'cisco',
       'port': 22,             # optional, default 22
       'secret': 'cisco',      # this is the enable password
       'verbose': True         # optional, default False
       }


connection = ConnectHandler(**cisco_device)

transfer_output = file_transfer(connection, source_file='ospf.txt', dest_file='ospf1.txt', file_system='nvram:', direction='put',
                                overwrite_file=True)
print('Closing connection')
connection.disconnect()