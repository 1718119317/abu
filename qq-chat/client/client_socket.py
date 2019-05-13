from client.config import *

from socket import *
ADDR=(HOST,PORT)
class ClientSocket():
    def __init__(self):
        self.create_socket()
        self.connect()

    def create_socket(self):
        self.sockfd=socket()
        # self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,DEBUG)

    # def bind(self):
    #     self.address=(gethostname(),5000)
    #     self.bind(self.address)
    #     self.ip = self.address[0]
    #     self.port = self.address[1]

    def connect(self):
        self.connect(ADDR)