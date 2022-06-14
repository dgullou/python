from netmiko import ConnectHandler

def execute(device,command):
       connection = ConnectHandler(**device)
       connection.enable()
       output = connection.send_config_set(command)
       print(output)
       connection.disconnect()

router1 = { 'device_type': 'cisco_ios', 'host': '192.168.59.171', 'username': 'cisco', 'password': 'cisco',
            'port': 22, 'secret': 'cisco', 'verbose': True }
cmd1 = ['router ospf 1', 'network 0.0.0.0 0.0.0.0 area 0']

router2 = { 'device_type': 'cisco_ios', 'host': '192.168.59.72', 'username': 'cisco', 'password': 'cisco',
            'port': 22, 'secret': 'cisco', 'verbose': True }
cmd2 = ['int loopback 0', 'ip address 1.1.1.1 255.255.255.255', 'end', 'sh ip int loopback 0']


router3 = { 'device_type': 'cisco_ios', 'host': '192.168.59.73', 'username': 'cisco', 'password': 'cisco',
            'port': 22, 'secret': 'cisco', 'verbose': True }
cmd3 = ['username k9 secret abck9', 'ip domain-name k9']
routers = [(router1,cmd1), (router2,cmd2), (router3,cmd3)]
for router in routers:
       execute(router[0],router[1])
