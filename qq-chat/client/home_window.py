import tkinter
from tkinter import ttk
from client.user_infos import UserInfo
from client.add_frend import AddFrend
from client.client_socket import ClientSocket
from threading import Thread
from client.handle_response import Response

# from PIL import Image,ImageTk
class Friends(ClientSocket):
    def __init__(self,name,friendlist):
        super().__init__()
        self.root=tkinter.Tk()
        #初始话时的好友列表
        self.friendlist=friendlist
        self.uname=name
        self.show()

    def show(self):
        root=self.root
        root.title("home")
        root.geometry("300x600+1000+0")

        # im=Image.open("color.jpg")
        # img=ImageTk.PhotoImage(im)
        # imLabel=tkinter.Label(root,image=img).pack()
        frm=tkinter.Frame(root,width=300,height=600)
        frm.pack()


        label_head=tkinter.Label(frm,text=self.uname)
        label_head["height"]=3
        # 绑定事件,鼠标单击时执行函数
        label_head.bind("<Button-1>",self.show_user_info)
        label_head.pack(anchor='nw')

        frm1=tkinter.Frame(frm)
        frm1.pack(anchor='e')

        # entry_add=tkinter.Entry(frm1)
        # entry_add.pack(anchor='w')

        label_search=tkinter.Label(frm1,text="添加")
        label_search.pack(anchor='e')
        #绑定事件,鼠标单击时执行函数
        label_search.bind("<Button-1>", self.add_friend)

        lb=tkinter.Listbox(frm)
        lb.pack()

        self.tree1=ttk.Treeview(lb)
        self.tree1.pack()

        #添加一级树枝
        self.treeF1=self.tree1.insert("",0,"好友",text="我的好友",values=("my_friends"))
        fres=self.friendlist

        #添加二级树枝
        for i in range(len(fres)):
            self.tree1.insert(self.treeF1, i, "", text=fres[i])

        self.tree1.bind("<Double-Button-1>",self.do_chat)
        handle_resp = Response()
        self.sockfd_udp.bind(self.sockfd.getsockname())
        recv_thread = Thread(target=handle_resp.handle_response)
        recv_thread.start()
        root.mainloop()

    def refresh_friendlist(self,friendlist):
        for item in self.treeF1.get_children():
            self.treeF1.delete(item)
        for i in range(len(friendlist)):
            self.tree1.insert(self.treeF1, i, "", text=friendlist[i])



    # def get_my_friends(self):
    #     fres = ["张三", "李四"]
    #     return fres

    def show_user_info(self,event):
        msg = 'UI ' + self.uname+" "+self.uname
        self.sockfd.send(msg.encode())
    def add_friend(self,event):
        adf=AddFrend(self.uname)
        adf.show()

    def do_chat(self,event):

        print(self.tree1.item(self.tree1.focus())['text'])

        # print("chat")

if __name__ == '__main__':
    fres_list=["zhang","赵敏","周芷若"]
    fre=Friends("zs",fres_list)
    fre.show()