"""
    套接字基类
"""

from client.config import *
from socket import *

ADDR=(HOST,PORT)
sockfd=socket()
sockfd.connect(ADDR)
sockfd_udp=socket(AF_INET,SOCK_DGRAM)
window_obj_list=[]

class ClientSocket():
    def __init__(self):

        #tcp套接字用于向服务端发送信息
        self.sockfd=sockfd

        #创建udp套接字用于接收服务端发来的信息
        self.sockfd_udp=sockfd_udp

        #设置全局变量,登陆后再赋值,把窗口对象添加到列表里
        self.window_obj_list=window_obj_list





if __name__ == '__main__':
    s=ClientSocket()
