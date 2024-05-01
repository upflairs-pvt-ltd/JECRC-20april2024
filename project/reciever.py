import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #
ip = "10.1.0.94"
port = 9999   # 0 -- 65536

complete_address = (ip,port)
s.bind(complete_address)

while True:
    data = s.recvfrom(120)
    message = data[0]
    message = message.decode('ascii')
    message = message+"\n"
    sender_ip = data[1][0]
    print(message)
    filename = sender_ip+".txt"
    with open(filename,'a+') as file:
        file.write(message)
    reply_mess = "Thanks for your awesome feedback"
    reply = reply_mess.encode('ascii')
    s.sendto(reply,sender_ip)
