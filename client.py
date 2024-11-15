import socket
import threading

#Procedure to get local IP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("1.1.1.1", 80))
local_ip = s.getsockname()[0]
s.close()

cli_addr = (local_ip, 5006)

def send_message():
    send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serv_ip = input("What is the server's IP address?: ")
    serv_port = int(input("What is the server's port number?: "))
    handshake = "handshake " + str(cli_addr[1])
    send_sock.sendto(handshake.encode(), (serv_ip, serv_port))
    while True:
        msg = input("")
        send_sock.sendto(msg.encode(), (serv_ip, serv_port))

def receive_message():
    rec_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    rec_sock.bind(cli_addr)
    while True:
        data, addr = rec_sock.recvfrom(1024)
        print("Serv: " + data.decode())

if __name__ == "__main__":
    rec = threading.Thread(target=receive_message)
    rec.start()
    send = threading.Thread(target=send_message)
    send.start()