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
#找出目前設備的提是符號
prompt = connection.find_prompt()
print(prompt)
if '>' in prompt:
       #進入CISCO的enable mode
       connection.enable()
# sending a command and getting the output
output = connection.send_command('sh run')
print(output)
# print(connection.check_config_mode())
#如果設備不在config mode則進入config mode
if not connection.check_config_mode():
       connection.config_mode()
connection.send_command('username u3 secret cisco')
connection.exit_config_mode()
# closing the connection
print('Closing connection')
connection.disconnect()