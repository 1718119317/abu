
from client.user_login import Login
from client.client_socket import ClientSocket
from threading import Thread
from client.home_window import Friends
from tkinter.messagebox import *

class Request(ClientSocket):


    def __init__(self,window_obj):
        super().__init__()
        self.window_obj=window_obj



    def request(self):
        while True:
            data=self.sockfd.recv(1024).decode().split()
            msg_type=data[0]
            if msg_type=="L":
                self.do_login_response(data)
            elif msg_type=="R":
                self.do_resgister_response(data)



    def do_login_response(self,data):
        if data[1]=="OK":
            self.window_obj.root.destroy()
            myuname=data[2]
            home = Friends(myuname)
            home.show()
        else:
            # showinfo("用户名或密码输入错误!!!")
            showinfo(data)

    def do_resgister_response(self,data):
        if data[1] == "OK":
            self.window_obj.reg.root.destroy()
            from client.user_login import Login
            myuname = data[2]
            login = Login(myuname)
        else:
            # showinfo("用户名或密码输入错误!!!")
            showinfo(data)






