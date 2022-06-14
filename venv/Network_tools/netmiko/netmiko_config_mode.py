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
print('Entering the golbal configuration mode ...')
connection.config_mode()
print('Creating a user...')
connection.send_command('username admin secret topsecret')
connection.exit_config_mode()
print('Saving the configuration...')
connection.send_command('write')

print(f'Closing connection from {cisco_device["host"]}')
connection.disconnect()