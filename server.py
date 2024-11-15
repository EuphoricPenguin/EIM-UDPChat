import socket
import threading

cli_addr = ()
serv_addr = ("127.0.0.1", 5005)

def send_message():
    global cli_addr
    send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        if cli_addr:
            msg = input("")
            send_sock.sendto(msg.encode(), cli_addr)

def receive_message():
    global cli_addr
    rec_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    rec_sock.bind(serv_addr)
    print("I'm listening at " + socket.gethostbyname(socket.gethostname()) + ":" + str(serv_addr[1]) + "!")
    #print("For local testing, use " + str(serv_addr[0]) + ":" + str(serv_addr[1]))
    while True:
        data, addr = rec_sock.recvfrom(1024)
        if data.decode().startswith("handshake"):
                cli_addr = (addr[0], int(data.decode().split(" ")[1]))
                #print(cli_addr)
                print("Connection established.")
        else:
            print("Cli: " + data.decode())

if __name__ == "__main__":
    rec = threading.Thread(target=receive_message)
    rec.start()
    send = threading.Thread(target=send_message)
    send.start()