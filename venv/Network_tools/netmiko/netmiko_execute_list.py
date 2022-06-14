from netmiko import ConnectHandler

def execute(device,command):
       connection = ConnectHandler(**device)
       connection.enable()
       output = connection.send_config_set(command)
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
cmd = ['no router rip', 'int loopback 0', 'ip address 1.1.1.1 255.255.255.255', 'end', 'sh ip int loopback 0']
execute(cisco_device,cmd)

