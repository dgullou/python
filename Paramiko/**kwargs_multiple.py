import define_paramiko

router1 = {'server_ip': '192.168.59.78', 'server_port':'22', 'user':'cisco', 'passwd': 'cisco'}
router2 = {'server_ip': '192.168.59.79', 'server_port':'22', 'user':'cisco', 'passwd': 'cisco'}
router3 = {'server_ip': '192.168.59.80', 'server_port':'22', 'user':'cisco', 'passwd': 'cisco'}
routers = [router1,router2,router3]

for router in routers:
    client = define_paramiko.connect(**router)
    shell = define_paramiko.get_shell(client)

    define_paramiko.send_command(shell, 'term len 0')
    define_paramiko.send_command(shell, 'enable')
    define_paramiko.send_command(shell, 'show run')

    output = define_paramiko.show(shell)
    #print(output)
    #將command的資訊切成每行放入list
    output_list = output.splitlines()
    print(output_list)
    #從第11開始之前的截斷
    output_list = output_list[11:-1]
    output = '\n'.join(output_list)
    print(output)

    router_file = define_paramiko.filename(router["server_ip"])

    with open(router_file, 'w') as f:
        f.write(output)
    define_paramiko.close(client)
