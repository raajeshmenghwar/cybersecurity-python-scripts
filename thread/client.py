#!/usr/bin/python3

import socket
import threading
import sys

sname = input("Set Client Name: ")

def send_mssg():
    while True:
        mssg = input(f"{sname} >> ").encode()

        if mssg.decode().lower() in ['q', 'exit']:
            print("Exiting the chat ....")
            s.send(f"{sname} has left the chat.".encode())
            s.close()
            sys.exit()

        s.send(f"{sname} : {mssg.decode()}".encode())  # Send message to the server

def recv_mssg():
    while True:
        received_mssg = s.recv(1024)  # Receive message from the server
        received_mssg = received_mssg.decode()  # Decode it to string

        if 'has left the chat' in received_mssg:
            print(f"\n{received_mssg}\nExiting the chat...")
            s.close()
            sys.exit()

        print(f"\r{received_mssg}\n{sname} >> ", end='')  # Print the received message and prompt


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Connecting....")
while True:
    try:
        s.connect(("127.0.0.1", 8888))  # Connect to the server
        break
    except ConnectionRefusedError:
        continue

print("Connected")

t1 = threading.Thread(target=send_mssg)
t1.start()

recv_mssg()
