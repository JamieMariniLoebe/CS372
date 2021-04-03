import socket

# PART 1
# Source for part 1: https://zetcode.com/python/socket/
# Was stuck for long time, this site helped a ton
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	host = "gaia.cs.umass.edu"
	port = 80

	s.connect((host, port)) #Connecting to host
	s.sendall(b"GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n") #Sending get request
	
	while True:

		data = s.recv(4096) #Receiving data

		if not data: #If no data received, break from loop
			break

		print("") #line break
		print(data.decode()) #Print out formatted data
	
	s.close()
