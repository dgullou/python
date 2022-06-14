
from netmiko import ConnectHandler
# creating a dictionary for the device to connect to
linux_host = {
       'device_type': 'linux',     #device type from https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py
       'host': '192.168.59.172',
       'username': 'jason',
       'password': 's8715024',
       'port': 22,             # optional, default 22
       'secret': 's8715024',      # sudo password
       'verbose': True         # optional, default False
       }

# connecting to the device and returning an ssh connection object
connection = ConnectHandler(**linux_host)
output = connection.send_command('cat /etc/hosts')
connection.enable() #sudo su
print(output)

print('Closing connection')
connection.disconnect()