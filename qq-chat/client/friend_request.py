import tkinter

import tkinter
from tkinter.messagebox import *
from client.home_window import Friends
from client.user_register import Register
from client.client_socket import ClientSocket
from client.user_infos import UserInfo
from tkinter.messagebox import *
"""
"""


class FriendRequest(ClientSocket):
    def __init__(self,data):

        # 设置tkinter窗口
        super().__init__()
        self.myuname = data[1]
        self.root = tkinter.Tk()
        self.uname=data[2]
        self.request_msg =data[3] # 元祖,包含用户名和请求信息
        self.show()

    def show(self):

        # 绘制label,grid（）确定行列
        self.user_uname=tkinter.Label(self.root, text=self.uname)
        self.user_uname.bind("<Button-1>",self.show_user_info)
        self.user_uname.grid(row=0)



        # 导入两个输入框
        self.e1 = tkinter.Text(self.root)
        self.e1.insert(tkinter.INSERT, self.request_msg)

        # 设置输入框的位置
        self.e1.grid(row=1, sticky=tkinter.W, padx=10, pady=5)


        # 设置两个按钮，点击按钮执行命令 command= 命令函数
        theButton1 = tkinter.Button(self.root, text="同意", width=10, command=self.agree_friend_request)
        theButton2 = tkinter.Button(self.root, text="拒绝", width=10, command=self.refuse_friend_request)


        # 设置按钮的位置行列及大小
        theButton1.grid(row=3, column=0, sticky=tkinter.W, padx=10, pady=5)
        theButton2.grid(row=3, column=1, sticky=tkinter.W, padx=10, pady=5)


        self.root.mainloop()

    def agree_friend_request(self):
        msg = 'FRR ' +"OK "+ self.myuname + ' ' +self.uname+" "+ self.request_msg
        self.sockfd.send(msg.encode())
        # data = self.sockfd.recv(1024).decode()
        # if data == "OK":
        #     showinfo("添加好友成功!!!")
        # else:
        #     showinfo(data)
        # self.root.destroy()

    def refuse_friend_request(self):
        refuse_msg=self.e1.get("0.0","end")
        msg = 'FRR ' +"NO "+ self.myuname + ' '+self.uname+ ' '+refuse_msg
        self.sockfd.send(msg.encode())

    def show_user_info(self,event):
        msg = 'UI ' + self.myuname+" "+self.uname
        self.sockfd.send(msg.encode())

if __name__ == '__main__':
    msg=("zs","我是张三")
    addfre=FriendRequest("ls",msg)
