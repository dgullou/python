import paramiko
import time
import getpass
# hostname = '192.168.59.78'
ssh_client = paramiko.SSHClient()
print(type(ssh_client))

# print(f'Connecting to {hostname}')
# ingore policy to choice if first use ssh to connect
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh_client.connect(hostname=hostname,port='22', username='cisco', password='cisco', look_for_keys=False, allow_agent=False)
#below need to use CLI to input password for secure
password = getpass.getpass('Enter password:')
router = {'hostname': '192.168.59.78', 'port':'22', 'username':'cisco', 'password': password}
print(f'Connecting to {router["hostname"]}')
ssh_client.connect(**router, look_for_keys=False, allow_agent=False)
#Input command
shell = ssh_client.invoke_shell()
shell.send('terminal length 0\n')
shell.send('show version\n')
shell.send('show ip int brief\n')
time.sleep(1)

output = shell.recv(10000)
output = output.decode('utf-8')
print(output)

# print(ssh_client.get_transport().is_active())
if ssh_client.get_transport().is_active() == True:
    print('Closing connection')
    ssh_client.close()
