import socket

HOST = "127.0.0.1"
PORT = 65000

#Source: https://realpython.com/python-sockets/#echo-server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    print("Enter /q to quit")
    print("Enter message to send")
    #If message is '/q' then QUIT program
        #CLOSE sockets
    #Else, continue to send message
    while True:
        message = input("> ")
        str_byte = str.encode(message)
        #If message is '/q'. then QUIT program
        #CLOSE sockets
        if(message == "\q"):
            s.close()
            exit()
        #Else, continue to send message
        else:
            s.sendall(str_byte)
            resp = s.recv(1024) #receive data
            #Source for decoding: https://stackoverflow.com/questions/41918836/how-do-i-get-rid-of-the-b-prefix-in-a-string-in-python
            print(resp.decode('utf-8'))
    