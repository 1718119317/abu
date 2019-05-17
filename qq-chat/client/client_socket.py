from client.config import *

from socket import *

ADDR=(HOST,PORT)
sockfd=socket()
sockfd.connect(ADDR)
window_obj_list=[]

class ClientSocket():
    def __init__(self):
        self.sockfd=sockfd
        #设置全局变量,登陆后再赋值
        self.window_obj_list=window_obj_list


    # def create_socket(self):
    #     self.sockfd=socket()
        # self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,DEBUG)

    # def bind(self):
    #     self.address=(gethostname(),5000)
    #     self.bind(self.address)
    #     self.ip = self.address[0]
    #     self.port = self.address[1]

    # def connect(self):
    #     self.sockfd.connect(ADDR)


if __name__ == '__main__':
    s=ClientSocket()
