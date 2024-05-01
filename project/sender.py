import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip = "10.1.0.94"
port = 9999

target_ip = (ip,port)
message = input("Write your message : ")
encrypt_message = message.encode("ascii")
s.sendto(encrypt_message,target_ip)
data = s.recvfrom(120)
print(data)