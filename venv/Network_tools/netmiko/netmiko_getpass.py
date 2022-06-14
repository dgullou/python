
from netmiko import ConnectHandler
import getpass
user_pass = getpass.getpass('Enter the user password:')


cisco_device = {
       'device_type': 'cisco_ios',
       'host': '192.168.59.171',
       'username': 'cisco',
       'password': user_pass,
       'port': '22',             # optional, default 22
       #'secret': 'cisco',      # this is the enable password
       'verbose': True         # optional, default False
       }

# connecting to the device and returning an ssh connection object
connection = ConnectHandler(**cisco_device)
#找出目前設備的提是符號
prompt = connection.find_prompt()
hostname = prompt[:-1]
print('hostname is '+hostname)


output1 = connection.send_command('sh ip interface bri')
output2 = connection.send_command('show arp')
filename1 = f'{hostname}-interface.txt'
filename2 = f'{hostname}-arp.txt'
with open(filename1,'w') as f1:
       f1.write(output1)
with open(filename2,'w') as f2:
       f2.write(output2)

print(f'Closing connection from {cisco_device["host"]}')
connection.disconnect()