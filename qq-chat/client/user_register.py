import tkinter
import json
# from client.user_login import Login
# import client.user_login
from tkinter.messagebox import *
# from client.home_window import Friends
from client.client_socket import ClientSocket


class Register(ClientSocket):
    def __init__(self):
        super().__init__()
        # self.window_obj_list.append(self)
        self.root=tkinter.Tk()
        self.show()

    def show(self):

        root=self.root
        root.title("注册")
        #窗口大小和窗口显示位置
        root.geometry("300x400+500+300")
        #绘制两个label,grid（）确定行列
        tkinter.Label(root,text="用户名：").grid(row = 0,column =0)
        tkinter.Label(root,text="年龄：").grid(row = 1,column =0)
        tkinter.Label(root,text="性别：").grid(row = 2,column =0)
        tkinter.Label(root,text="地址：").grid(row = 3,column =0)
        tkinter.Label(root,text="手机号：").grid(row = 4,column =0)
        tkinter.Label(root,text="密  码：").grid(row = 5,column =0)

        #下面输入款绑定的变量,用于后续对输入框的取值和赋值
        self.uname=tkinter.StringVar()
        self.uage=tkinter.StringVar()
        self.usex=tkinter.StringVar()
        self.uaddr=tkinter.StringVar()
        self.utel=tkinter.StringVar()
        self.upasswd=tkinter.StringVar()

        #导入两个输入框
        e1 = tkinter.Entry(root,textvariable=self.uname)
        e2 = tkinter.Entry(root,textvariable=self.uage)
        e3 = tkinter.Entry(root,textvariable=self.usex)
        e4 = tkinter.Entry(root,textvariable=self.uaddr)
        e5 = tkinter.Entry(root,textvariable=self.utel)
        e6 = tkinter.Entry(root,textvariable=self.upasswd)

        #设置输入框的位置
        e1.grid(row =0 ,column =1,sticky =tkinter.W, padx=10,pady =5)
        e2.grid(row =1 ,column =1,sticky =tkinter.W, padx=10,pady =5)
        e3.grid(row =2 ,column =1,sticky =tkinter.W, padx=10,pady =5)
        e4.grid(row =3 ,column =1,sticky =tkinter.W, padx=10,pady =5)
        e5.grid(row =4 ,column =1,sticky =tkinter.W, padx=10,pady =5)
        e6.grid(row =5 ,column =1,sticky =tkinter.W, padx=10,pady =5)



        #设置两个按钮，点击按钮执行命令 command= 命令函数
        theButton1 = tkinter.Button(root, text ="注册", width =10,command =self.do_register)
        theButton2 = tkinter.Button(root, text ="重置",width =10,command =self.do_reset)

        #设置按钮的位置行列及大小
        theButton1.grid(row =7 ,column =0,sticky =tkinter.W, padx=10,pady =5)
        theButton2.grid(row =7 ,column =1,sticky =tkinter.E, padx=10,pady =5)
        root.mainloop()

    def do_register(self):
        dict_uinfo={}
        dict_uinfo["uname"]=self.uname.get()
        dict_uinfo["uage"]=self.uage.get()
        dict_uinfo["usex"]=self.usex.get()
        dict_uinfo["utel"]=self.utel.get()
        dict_uinfo["uaddr"]=self.uaddr.get()
        dict_uinfo["upasswd"]=self.upasswd.get()
        #将用户信息字典转成字符串发送
        msg = 'R ' +json.dumps(dict_uinfo)
        self.sockfd.send(msg.encode())
        data = self.sockfd.recv(128).decode().split()
        if data[1] == "OK":
            self.root.destroy()
            from client.user_login import Login
            myuname = data[2]
            Login(myuname)

        else:
            # showinfo("用户名或密码输入错误!!!")
            showinfo(data)


    def do_reset(self):
        self.uname.set("")
        self.uage.set("")
        self.usex.set("")
        self.uaddr.set("")
        self.utel.set("")
        self.upasswd.set("")


if __name__ == '__main__':
    reg=Register()

