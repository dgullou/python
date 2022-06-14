from netmiko import ConnectHandler

def execute(device,command):
       connection = ConnectHandler(**device)
       output = connection.send_command(command)
       print(output)
       connection.disconnect()

cisco_device = {
       'device_type': 'cisco_ios',
       'host': '192.168.59.171',
       'username': 'cisco',
       'password': 'cisco',
       'port': '22',             # optional, default 22
       #'secret': 'cisco',      # this is the enable password
       'verbose': True         # optional, default False
}

execute(cisco_device,'show version')

linux = {
    'device_type': 'linux',
    'host': '192.168.59.172',
    'username': 'jason',
    'password': 's8715024',
    'port': 22,
    'secret': 'softjack',
    'verbose': True
}
execute(linux, 'ifconfig')
