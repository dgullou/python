
from netmiko import ConnectHandler
import logging
import time
logging.basicConfig(filename='test.log',level=logging.DEBUG)
logger = logging.getLogger("netmiko")
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
# output = connection.send_command('show version')
# print(output)
# or
connection.write_channel('show version\n')
time.sleep(2)
output = connection.read_channel()
print(output)

print('Closing connection')
connection.disconnect()