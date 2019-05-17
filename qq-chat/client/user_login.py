import tkinter
from tkinter.messagebox import *
from client.home_window import Friends
from client.user_register import Register
from client.client_socket import ClientSocket
"""
"""

class Login(ClientSocket):
    def __init__(self,uname=""):

        # 设置tkinter窗口
        super().__init__()
        self.save_uname=uname
        self.root = tkinter.Tk()
        self.show()


    def show(self):

        #绘制两个label,grid（）确定行列
        tkinter.Label(self.root,text="用户名：").grid(row = 0,column =0)
        tkinter.Label(self.root,text="密  码：").grid(row = 1,column =0)
        
        self.uname=tkinter.StringVar()

        self.upasswd=tkinter.StringVar()
        #导入两个输入框
        e1 = tkinter.Entry(self.root,textvariable=self.uname)
        e2 = tkinter.Entry(self.root,textvariable=self.upasswd)

        #设置输入框的位置
        e1.grid(row =0 ,column =1,sticky =tkinter.W, padx=10,pady =5)
        e2.grid(row =1 ,column =1,sticky =tkinter.W, padx=10,pady =5)


        #设置两个按钮，点击按钮执行命令 command= 命令函数
        theButton1 = tkinter.Button(self.root, text ="登录", width =10,command =self.do_login)
        theButton2 = tkinter.Button(self.root, text ="注册",width =10,command =self.do_resgister)

        #设置按钮的位置行列及大小
        theButton1.grid(row =3 ,column =0,sticky =tkinter.W, padx=10,pady =5)
        theButton2.grid(row =3 ,column =1,sticky =tkinter.E, padx=10,pady =5)
        self.uname.set(self.save_uname)
        self.root.mainloop()

    def do_login(self):
        name=self.uname.get()
        passwd=self.upasswd.get()
        msg='L '+name+' '+passwd
        self.sockfd.send(msg.encode())
        data=self.sockfd.recv(1024).decode()
        if data=="OK":
            # self.myuname=name #把name赋值给全局变量,方便各个串口
            self.root.destroy()
            home = Friends(name)
            home.show()
        else:
            # showinfo("用户名或密码输入错误!!!")
            showinfo(data)

        # print(self.uname.get(),self.upasswd.get())



    def do_resgister(self):

        self.root.destroy()
        reg=Register()

        # self.root.quit()



if __name__ == '__main__':


    login=Login()


