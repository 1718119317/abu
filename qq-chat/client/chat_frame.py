import tkinter
from tkinter import scrolledtext
from tkinter import END
from client.client_socket import ClientSocket
from time import ctime


class ChatFrame(ClientSocket):
    def __init__(self,user1,user2):
        super().__init__()
        self.window_obj_list.append(self)
        self.user1 = user1
        self.user2 = user2
        self.root = tkinter.Tk()
        # self.show1()

    def show1(self,data=""):
        self.root.title(self.user2)
        self.root.geometry('+400+200')

        # 创建多行文本框
        self.msgBox = tkinter.Listbox(self.root, width=60, height=20)
        self.msgBox.grid(row=0,columnspan=3)

        # 创建输入文本框和关联变量
        self.a = tkinter.StringVar()
        self.a.set('')
        self.msg_send = tkinter.Entry(self.root,width=50,textvariable=self.a)
        self.msg_send.grid(row=2,columnspan=2)


        # 创建发送按钮
        sendbutton = tkinter.Button(self.root, text='发送', command=self.send_msg1)
        sendbutton.grid(row=2,column=2)
        self.root.bind('<Return>', self.send_msg)  # 绑定回车发送信息
        if data:
            self.show_msg(data)

        #关闭窗口时执行事件
        self.root.protocol("WM_DELETE_WINDOW",self.close_window)


        self.root.mainloop()

    # 用于时刻接收服务端发送的信息并输出在msgBox中
    def show_msg(self,data):
        print("xianshi"," ".join(data[4:]))
        self.msgBox.insert(END, " ".join(data[4:]))
        self.msgBox.insert(END, data[3])


    def send_msg(self,event):
        msg1 =self.user1+":"+ self.msg_send.get()
        msg2 = ctime()
        msg = 'C ' + self.user1 + ' ' + self.user2 + ' ' + msg1+' '+msg2
        self.sockfd.send(msg.encode())
        self.msgBox.insert(END,msg2)
        self.msgBox.insert(END, msg1)
        self.a.set('')

    def send_msg1(self):
        msg1 = self.user1+":"+ self.msg_send.get()
        msg2 = ctime()
        msg = 'C ' + self.user1 + ' ' + self.user2 + ' ' + msg1+' '+msg2
        self.sockfd.send(msg.encode())
        self.msgBox.insert(END,msg2)
        self.msgBox.insert(END, msg1)
        self.a.set('')

    def close_window(self):
        self.window_obj_list.remove(self)
        self.root.destroy()
        print(self.window_obj_list)







if __name__=="__main__":
    # def startChatFrame():
    #     chat = ChatFrame("lisi","ww")
    #     chat.show()

    ChatFrame("lisi","ww").show()