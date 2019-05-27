"""
    接收服务端发来的信息并处理
"""

from client.client_socket import ClientSocket
from threading import Thread

from tkinter.messagebox import *
from client.user_infos import UserInfo
import json
from tkinter.messagebox import *
from client.chat_frame import ChatFrame

class Response(ClientSocket):

    def __init__(self):
        super().__init__()

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
            elif msg_type == "C":
                self.do_chat(data)

    #处理聊天信息
    def do_chat(self,data):
        friend_chat=self.__find_chat_window(data[2])
        # print(friend_chat,self.window_obj_list)
        if friend_chat:
            friend_chat.show_msg(data)
        else:
            def chat(data):
                friend_chat=ChatFrame(data[1], data[2])
                friend_chat.show1(data)
            chat=Thread(target=chat,args=(data,))
            chat.start()

    #处理拒绝添加好友信息
    def do_friend_request_result(self,data):
        if data[1]=="OK":
            showinfo(data[2])
            self.__find_chat_window("home").refresh_friendlist(data[3:])
        else:
            showinfo(data[2])

    #处理添加好友请求信息
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
        # res=data[2:]
        print(self.window_obj_list,self.window_obj_list[0].root.title())
        af=self.__find_chat_window("add_friend")
        af.show_search(data[2:])


    #显示个人信息结果
    def show_user_info(self,data):
        str="".join(data[2:])
        dict_uinfo=json.loads(str)
        UserInfo(dict_uinfo)









