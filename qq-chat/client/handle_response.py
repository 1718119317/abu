

from client.client_socket import ClientSocket
from threading import Thread

from tkinter.messagebox import *
from client.user_infos import UserInfo
import json
from tkinter.messagebox import *

class Response(ClientSocket):


    def __init__(self):
        super().__init__()
        # self.window_obj=window_obj



    def handle_response(self):
        while True:
            print("等待接收:...",self.sockfd_udp.getsockname())
            data,server_addr=self.sockfd_udp.recvfrom(1024)
            data=data.decode().split()
            print("Receive message:",data)
            msg_type=data[0]
            if msg_type=="UI":
                self.show_user_info(data)
            elif msg_type=="SU":
                self.do_search_user(data)
            elif msg_type=="FR":
                self.do_friend_request(data)
            elif msg_type=="FRR":
                self.do_friend_request_result(data)

    def do_friend_request_result(self,data):
        if data[1]=="OK":
            showinfo(data[2])
            self.__find_chat_window("home").refresh_friendlist(data[3:])
        else:
            showinfo(data[2])

    def do_friend_request(self,data):
        from client.friend_request import FriendRequest
        fr=FriendRequest(data)


    #查找窗口实例化对象
    def __find_chat_window(self,obj_name):
        for item in self.window_obj_list:
            if item.root.title()==obj_name:
                return item

    #显示查询用户结果
    def do_search_user(self,data):
        res=data[2:]
        print(self.window_obj_list,self.window_obj_list[0].root.title())
        af=self.__find_chat_window("add_friend")
        af.show_search(data[2:])


    #显示个人信息结果
    def show_user_info(self,data):
        # uname=data[1]
        # print(data[2],len(data))
        str="".join(data[2:])
        dict_uinfo=json.loads(str)
        UserInfo(dict_uinfo)









