# from netmiko import Netmiko
# connection = Netmiko(host='10.1.1.10', port='22', username='u1', password='cisco', device_type='cisco_ios')

from netmiko import ConnectHandler
from datetime import datetime
import time
import threading

start = time.time()

def backup(device):
       connection = ConnectHandler(**device)
       print('entering the enable mode...')
       connection.enable()
       output = connection.send_command('show run')
       prompt = connection.find_prompt()
       hostname = prompt[0:-1]
       now = datetime.now()
       year = now.year
       month = now.month
       day = now.day
       filename = f'{hostname}_{year}--{month}--{day}_backup.txt'
       with open(filename, 'w') as backup:
              backup.write(output)
              print(f'Backup of {hostname} completed successfully')
              print('#' * 30)
       print('Closing connection')
       connection.disconnect()


with open('device.txt') as f:
       devices = f.read().splitlines()

threads = list()
for ip in devices:
       device = {
              'device_type': 'cisco_ios',
              'host': ip,
              'username': 'cisco',
              'password': 'cisco',
              'port': 22,
              'secret': 'cisco',
              'verbose': True
              }
       th = threading.Thread(target=backup,args=(device,))
       threads.append(th)

for th in threads:
       th.start()

for th in threads:
       th.join()
end = time.time()
print(f'Total execution time:{end-start}')




