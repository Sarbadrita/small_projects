import socket
import threading

nickname= input("choose a nickname")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.1.104' , 55555))

def receive():
    try:
        while True:

            msg = client.recv(2024).decode()

            if msg == 'NICK':
                client.send(nickname.encode())
            else:
                print(msg)

    except Exception as err:
        print("an error occurred")
        #client.close()
        #print('client needs to close')
        print(err)
        #break

def write():
    while True:
        m1 = input(str())

        msg = f'{nickname} : {m1}'
        #print(msg)
        client.send(msg.encode())
        #print(msg)

rcv_thread = threading.Thread(target=receive)
rcv_thread.start()

wrt_thread = threading.Thread(target=write)
wrt_thread.start()



