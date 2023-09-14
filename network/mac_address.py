def generate_mac_addresses(starting_mac, count):
    mac_addresses = []

   
    current_mac = int(starting_mac, 16)

    for _ in range(count):
        # 将当前MAC地址格式化为12个字符的十六进制字符串
        mac_str = format(current_mac, '012x')
        mac_addresses.append(mac_str)

        # 递增MAC地址
        current_mac += 1

    return mac_addresses

starting_mac = '000000000011'
count = 512

mac_addresses = generate_mac_addresses(starting_mac, count)

for mac in mac_addresses:
    print(mac)
