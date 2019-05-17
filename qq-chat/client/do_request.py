
from client.user_login import Login
from client.client_socket import ClientSocket
from threading import Thread

class Request(ClientSocket):
    def __init__(self,window_obj):
        self.window_obj=window_obj



    def request(self):
        while True:
            data=self.sockfd.recv(1024).decode().split()
            msg_type=data[0]
            if msg_type=="L":
                self.do_login_response(data)



    def do_login_response(self,data):
        if data[1]=="OK":
            self.window_obj.destory()







