#!/usr/bin/python3           # This is client.py file 
import socket
# create a socket object 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
# get local machine name 
host = socket.gethostname()                            
port = 9999

# connection to hostname on the port. 
s.connect((host, port))
s.send("hello There".encode('ascii'))
# Receive no more than 1024 bytes 
msg = s.recv(1024)
print(msg)
x = input("Press any value + [Enter]...")
if x is not None:
    s.close() 