import socket

# PART 2
# Source: https://stackoverflow.com/questions/17667903/python-socket-receive-large-amount-of-data
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    host = "gaia.cs.umass.edu"
    port = 80

    s.connect((host, port)) #Connect to host
    s.sendall(b"GET /wireshark-labs/HTTP-wireshark-file3.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n") #Send GET request
    
    while True:

        data = s.recv(4096) #Receive data

        if not data: #Break if no more data received
            break
        print("")

        print(data.decode())
    s.close() #Close connection