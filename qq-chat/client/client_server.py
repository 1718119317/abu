from socket import *
from client.user_login import Login
from client.client_socket import ClientSocket

"""
客户端服务器,创建套接字连接,用于与后端服务器交互
"""

class ClientServer():
    def __init__(self):
        self.sockfd=ClientSocket()


    #客户端启动则连接客户端,并开启登录窗口
    def start(self):
        login=Login()
        login.show()