# from netmiko import Netmiko
# connection = Netmiko(host='10.1.1.10', port='22', username='u1', password='cisco', device_type='cisco_ios')

from netmiko import ConnectHandler
with open('device.txt') as f:
       devices = f.read().splitlines()

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

       connection = ConnectHandler(**cisco_device)
       print('entering the enable mode...')
       connection.enable()

       output = connection.send_command('show run')
       prompt = connection.find_prompt()
       #扣掉最後一位EX: R1#就會去掉#
       hostname = prompt[0:-1]
       from datetime import datetime
       now = datetime.now()
       year = now.year
       month = now.month
       day = now.day
       filename = f'{hostname}_{year}--{month}--{day}_backup.txt'
       with open(filename, 'w') as backup:
              backup.write(output)
              print(f'Backup of {hostname} completed successfully')
              print('#'*30)
       print('Closing connection')
       connection.disconnect()
