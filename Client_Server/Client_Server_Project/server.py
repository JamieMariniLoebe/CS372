import socket

HOST = '127.0.0.1'
PORT = 65000

#Source: https://realpython.com/python-sockets/#echo-server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #For using same port #
    s.bind((HOST,PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Connected by ", addr)
        first_req = conn.recv(1024) #Receiving first message from client
        print(first_req.decode('utf-8'))

        print("\nEnter /q to quit")
        print("Enter message to send")
        while True:
            val = input("> ") #Prompt for user input
            message = str.encode(val) #Encode message from string to bytes
            #If message is '/q'. then QUIT program
            #CLOSE sockets
            if(val == "\q"):
                s.close()
                exit()
            #Else, continue to send the reply
            else:
                conn.sendall(message) #Send message to client
                reply = conn.recv(1024)
                #Source for decoding: https://stackoverflow.com/questions/41918836/how-do-i-get-rid-of-the-b-prefix-in-a-string-in-python
                print(reply.decode('utf-8'))
