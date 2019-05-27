#　tcp_server.py  重要

import socket
from models import StudentModel


#　TCP创建套接字
sockfd = socket.socket(socket.AF_INET,\
    socket.SOCK_STREAM)

#　绑定地址
sockfd.bind(('127.0.0.1',8886))

#　设置监听
sockfd.listen(3)

#　等待客户端连接
while True:
    print("Waiting for connect ....")
    try:
        connfd,addr = sockfd.accept()
    except KeyboardInterrupt:
        print("Server exit")
        break
    print("Connect from",addr) #　客户端地址

    # 消息收发
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        data=data.decode
        print("Receive message:",data)

        print(type(data))
        print(data.id,data.name,data.age)

        n = connfd.send(b"Receive your message")
        print("Send %d bytes"%n)
    connfd.close()

 # 关套接字
sockfd.close()






