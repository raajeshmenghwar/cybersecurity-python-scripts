#!/usr/bin/python3

import socket
import threading
import sys

sname = input("Set Server Name: ")

def send_mssg():
    while True:
        mssg = input(f"{sname} >> ").encode()

        if mssg.decode().lower() in ['q', 'exit']:
            print("Exiting the chat ....")
            client.send(f"{sname} has left the chat.".encode()) 
            s.close()
            sys.exit()

        client.send(f"{sname} : {mssg.decode()}".encode())  # Send the message to the client

def recv_mssg():
    while True:
        received_mssg = client.recv(1024)  # Receive the message from the client
        received_mssg = received_mssg.decode()  # Decode it to string

        if 'has left the chat' in received_mssg:
            print(f"\n{received_mssg}\nExiting the chat...")
            client.close()
            sys.exit()

        print(f"\r{received_mssg}\n{sname} >> ", end='')  # Print the received message and prompt


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("127.0.0.1", 8888))
print("Listening...")
s.listen(1)

client, add = s.accept()

print("Connected")

t1 = threading.Thread(target=send_mssg)
t1.start()

recv_mssg()
