import threading
import socket

host = '192.168.1.104'
port = 55555

server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))                                    # binding server
server.listen()                                             # server listening for connections

clients=[]
nicknames=[]

# broadcasting

def brod(msg):
    #print("hello")
    for client in clients:
        client.send(msg)

def handle(client):
    while True:
        try:
            msg = client.recive(2024)
            brod(msg)

        except :
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname= nicknames[index]
            brod(f'{nickname} left the chat! :('.encode())
            nicknames.remove(nickname)
            break

# receive function
def receive():
    while True:
        client, addr=server.accept()
        #print(client)
        print(f"connected with {str(addr)}")

        # receiving nickname
        client.send('NICK'.encode())
        nickname = client.recv(1024).decode()
        nicknames.append(nickname)
        #print(nicknames)
        clients.append(client)
        #print(clients)

        print(f'nickname of the client is {nickname}')
        noti = f'{nickname} joined the chat !'.encode()
        brod(noti)
        client.send('connected to the server'.encode())

        # assigning thread to each client's operation for efficiency
        thread = threading.Thread(target=handle , args=(client,))
        thread.start()


print("server is listening")
receive()




