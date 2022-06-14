# from netmiko import Netmiko
# connection = Netmiko(host='10.1.1.10', port='22', username='u1', password='cisco', device_type='cisco_ios')

from netmiko import ConnectHandler
with open('device.txt') as f:
       devices = f.read().splitlines()
device_list = list()
for ip in devices:
       cisco_device = {
              'device_type': 'cisco_ios',
              'host': ip,
              'username': 'cisco',
              'password': 'cisco',
              'port': 22,
              'secret': 'cisco',
              'verbose': True
       }
       device_list.append(cisco_device)

for device in device_list:
       connection = ConnectHandler(**device)
       print('entering the enable mode...')
       connection.enable()
       file = input(f'enter a configuration file (use a valid path) for {device["host"]}:')
       print(f'running commands from file:{file} on device: {device["host"]}')
       output = connection.send_config_from_file(file)
       print(output)
       print(f'Closing connect to {cisco_device["host"]}')
       connection.disconnect()
       print('#'*30)