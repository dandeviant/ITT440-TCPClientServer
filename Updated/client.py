# Import socket module
import socket            
import os
 
# Create a socket object
s = socket.socket()        
 
# Define the port on which you want to connect
port = 8080               
 
# connect to the server on local computer
s.connect(('192.168.246.139', port))
 
#Ping to server
command = "hostname -I"
output = os.popen(command)
ip = output.read()
print("Message = %s" %(ip))

addr = ("192.168.246.139", port)

msg = bytes(ip, "utf-8")
s.sendto(msg, addr)


# receive data from the server and decoding to get the string.
print (s.recv(1024).decode())
# close the connection
s.close()  
