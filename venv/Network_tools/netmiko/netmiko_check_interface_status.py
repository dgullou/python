
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
connection.send_command('terminal lenghth 0')

interface = input('Enter the enteries you want to enable:')
output = connection.send_command('show ip interface ' + interface)
# first_line = output.splitlines()
# print(first_line)

if 'Invalid input detected' in output:
       print('You entered invalid interface')
else:
       first_line = output.splitlines()[0]
       print(first_line)
       if not 'up' in first_line:
              print('The interface is down. Enablbing the interface ...')
              commands = ['interface ' + interface, 'no shut', 'exit' ]
              output = connection.send_config_set(commands)
              print(output)
              print('#' * 40)
              print('The interface has been enabled')
       else:
              print('interface ' + interface + 'is already enabled.')

print('Closing connection')
connection.disconnect()