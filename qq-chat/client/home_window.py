import tkinter
from tkinter import ttk
from client.user_infos import UserInfo
from client.add_frend import AddFrend
from client.client_socket import ClientSocket
# from PIL import Image,ImageTk
class Friends(ClientSocket):
    def __init__(self,name):
        super().__init__()
        self.root=tkinter.Tk()
        self.uname=name
        self.show()

    def show(self):
        root=self.root
        root.title("好友")
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
        label_head.bind("<Button-1>", self.add_friend)

        lb=tkinter.Listbox(frm)
        lb.pack()

        tree1=ttk.Treeview(lb)
        tree1.pack()

        #添加一级树枝
        treeF1=tree1.insert("",0,"好友",text="我的好友",values=("my_friends"))
        fres=self.get_my_friends()

        friends = []
        #添加二级树枝
        for i in range(len(fres)):
            tree1.insert(treeF1, i, "", text=fres[i])
        # for i in range(len(friends)):
        #     friends[i].bind("<Double-Button-1>",self.do_chat)
        tree1.bind("<Double-Button-1>",self.do_chat)
        root.mainloop()

    def get_my_friends(self):
        fres = ["张三", "李四"]
        return fres

    def show_user_info(self,event):
        uinfo=UserInfo(self.uname)
        uinfo.show()
    def add_friend(self,event):
        adf=AddFrend(self.uname)
        adf.show()

    def do_chat(self,event):

        print("chat")

if __name__ == '__main__':
    fre=Friends("zs")
    fre.show()