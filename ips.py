import ipaddress

ip = '192.168.0.1'
endereco = ipaddress.ip_address(ip)
print(endereco + 2000)

ip1 = '192.168.0.1/24'
rede = ipaddress.ip_network(ip1, strict=False)
print(rede)