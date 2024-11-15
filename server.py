import socket
import threading

#Procedure to get local IP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("1.1.1.1", 80))
local_ip = s.getsockname()[0]
s.close()

cli_addr = ()
serv_addr = (local_ip, 5005)

def send_message():
    global cli_addr
    cli_connect = True
    send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        if cli_addr:
            if cli_connect:
                # Sends confirmation to client of connection.
                send_sock.sendto(b"Connection established.", cli_addr)
                cli_connect = False
            msg = input("")
            send_sock.sendto(msg.encode(), cli_addr)

def receive_message():
    global cli_addr
    global cli_connect
    rec_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    rec_sock.bind(serv_addr)
    print("I'm listening at " + serv_addr[0] + ":" + str(serv_addr[1]) + "!")
    while True:
        data, addr = rec_sock.recvfrom(1024)
        if data.decode().startswith("handshake"):
                cli_addr = (addr[0], int(data.decode().split(" ")[1]))
                print("Connection established.")
        else:
            print("Cli: " + data.decode())

if __name__ == "__main__":
    rec = threading.Thread(target=receive_message)
    rec.start()
    send = threading.Thread(target=send_message)
    send.start()