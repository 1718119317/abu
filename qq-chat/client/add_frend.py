import tkinter
from tkinter import ttk
from client.client_socket import ClientSocket
from tkinter.messagebox import *

# from PIL import Image,ImageTk
class AddFrend(ClientSocket):
    def __init__(self,uname):
        super().__init__()
        self.uname = uname
        self.root=tkinter.Tk()
    
    def show(self):
        root=self.root
        root.title("添加")
        root.geometry("300x600+1000+0")
        
        # im=Image.open("color.jpg")
        # img=ImageTk.PhotoImage(im)
        # imLabel=tkinter.Label(root,image=img).pack()

        frm=tkinter.Frame(root,width=300,height=600)
        frm.pack()
        
        entry_add=tkinter.Entry(frm)
        entry_add.pack(anchor='w')
        
        label_search=tkinter.Label(frm,text="搜索")
        label_search.bind("<Button-1>", self.search_by_name)
        label_search.pack(anchor='e')

        global listbox_show
        listbox_show=tkinter.Listbox(frm)
        listbox_show.pack()

        root.mainloop()

    def send_friend_request(self):
        user_uname="zhang"
        msg = 'A ' + self.uname + ' ' + user_uname+" 我是XXX,想添加你为好友!"
        self.sockfd.send(msg.encode())
        data = self.sockfd.recv(1024).decode()
        if data == "OK":
            showinfo("添加好友成功!!!")
        else:
            showinfo(data)

    def search_by_name(self,event):
        res = ["张三", "李四"]
        for item in res:
            tkinter.Label(listbox_show, text=item).pack()
        print(res)

if __name__ == '__main__':
    add=AddFrend("zs")
    add.show()