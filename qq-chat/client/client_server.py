"""
客户端服务器
"""

from client.user_login import Login
from client.client_socket import ClientSocket



class ClientServer(ClientSocket):
    def __init__(self):

        super().__init__()
        self.start()

    #客户端启动则连接客户端,并开启登录窗口
    def start(self):

        login=Login()





