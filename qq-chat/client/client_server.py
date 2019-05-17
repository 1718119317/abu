from socket import *
from client.user_login import Login
from client.client_socket import ClientSocket
from threading import Thread
from client.do_request import Request

"""
客户端服务器,创建套接字连接,用于与后端服务器交互
"""

class ClientServer(ClientSocket):
    def __init__(self):
        super().__init__()
        # self.sockfd=ClientSocket()
        # self.create_socket()
        # self.connect()
        self.start()

    #客户端启动则连接客户端,并开启登录窗口
    def start(self):

        login=Login()
        re=Request(login)
        recv_thread=Thread(target=re.request)
        recv_thread.start()



