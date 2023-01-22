#!/bin/python3

import socket
from IPy import IP

def scan_port(ipaddress,port):
	try:
		sock = socket.socket()
		sock.settimeout(0.5)
		sock.connect((ipaddress,port))
		print('[*] port ' + str(port) + ' is open')
	except:
		print('[*] port ' + str(port) + ' is closed')

ipaddress = input('[*] Enter the target to scan: ')
for port in range(1,101):
	scan_port(ipaddress,port)
