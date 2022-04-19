import paramiko
import time

def connect(server_ip, server_port, user, passwd):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f'Connecting to {server_ip}')
    ssh_client.connect(hostname=server_ip, port=server_port, username=user, password=passwd, look_for_keys=False, allow_agent=False)
    return ssh_client

def get_shell(ssh_client):
    shell = ssh_client.invoke_shell()
    return shell

def send_command(shell, command, timeout=1):
    print(f'Send command: {command}')
    shell.send(command + '\n')
    time.sleep(timeout)

def show(shell, n=10000):
    output = shell.recv(n)
    return output.decode()

def close(ssh_client):
    if ssh_client.get_transport().is_active() == True:
        print('Closing connection')
        ssh_client.close()

def filename(ip_address):
    from datetime import datetime
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    routerip = ip_address
    file_name = f'{routerip}_{year}--{month}--{day}.txt'
    return file_name

if __name__ == '__main__':
    router1 = {'server_ip': '192.168.59.78', 'server_port': '22', 'user': 'cisco', 'passwd': 'cisco'}
    client = connect(**router1)
    # client = connect('192.168.59.78','22','cisco','cisco')
    shell = get_shell(client)
    send_command(shell, 'enable')
    # send_command(shell, 'cisco')
    send_command(shell, 'term len 0')
    send_command(shell, 'sh version')
    send_command(shell, 'sh ip int brief')
    output = show(shell)
    #print(output)
    # from datetime import datetime
    #
    # now = datetime.now()
    # year = now.year
    # month = now.month
    # day = now.day
    # hour = now.hour
    # minute = now.minute
    # file_name = f'{router1["server_ip"]}_{year}--{month}--{day}.txt'
    # print(file_name)
    router_file = filename(router1["server_ip"])
    print(router_file)


    # with open(router_config,'w') as f:
    #     f.write(output)
    close(client)
