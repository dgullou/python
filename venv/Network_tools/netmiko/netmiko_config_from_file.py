from netmiko import ConnectHandler

cisco_device = {
       'device_type': 'cisco_ios',
       'host': '192.168.59.171',
       'username': 'cisco',
       'password': 'cisco',
       'port': '22',             # optional, default 22
       #'secret': 'cisco',      # this is the enable password
       'verbose': True         # optional, default False
       }

# connecting to the device and returning an ssh connection object
connection = ConnectHandler(**cisco_device)

print('Entering the enable mode ...')
connection.enable()


print('Sending commands from file ...')
output = connection.send_config_from_file('rip.txt')
print(output)

print(f'Closing connection from {cisco_device["host"]}')
connection.disconnect()