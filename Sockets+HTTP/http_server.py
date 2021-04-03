import socket

# PART 3
# Source: https://www.codementor.io/@joaojonesventura/building-a-basic-http-server-from-scratch-in-python-1cedkg0842
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    host = "127.0.0.1"
    port = 1250

    s.bind((host,port))
    s.listen()
    connectSocket, addr = s.accept()
    with connectSocket:
        message = connectSocket.recv(1250).decode()
        print("RECEIVED: " + message)
        print("")
        print("")
        data = "HTTP/1.1 200 OK\r\n"\
        "Content-Type: text/html; charset=UTF-8\r\n\r\n"\
        "<html>Congratulations! You've downloaded the first Wireshark lab file!</html>\r\n"
        print('SENDING ' + data)
        connectSocket.sendall(data.encode())
        
