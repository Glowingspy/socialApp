import socket
import threading

#maybe make a list to handle clients to see how many connections i get a day

HEADER = 64
PORT = 5050 
SERVER = socket.gethostbyname(socket.gethostname())
print(SERVER)
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT = '!DISCONNE45CT!\?<>'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f'New {addr}, connected.')

    connected = True
    while connected:
        info_length = conn.recv(HEADER).decode(FORMAT)
        if info_length:
            info_length = int(info_length)
            info = conn.recv(info_length).decode(FORMAT)
            print(f'Information coming from {addr} saying: {info}')
            if info == DISCONNECT:
                print(f'{ADDR} has disconnected. Current active connections are {threading.activeCount() - 2}')
                connected = False 
    
    conn.close()

def start():
    server.listen()
    print(f'Server is running on, {SERVER}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'Active connections, {threading.activeCount() - 1}')

print('Listening... ', end='')
start()