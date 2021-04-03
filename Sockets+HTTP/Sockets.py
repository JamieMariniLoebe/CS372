import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	host = "gaia.cs.umass.edu"
	port = 80

	s.connect((host, port))
	print 'Socket created'