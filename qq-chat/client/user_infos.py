"""
    显示用户信息窗口
"""

import tkinter
from client.client_socket import ClientSocket

class UserInfo(ClientSocket):
    def __init__(self,dict_uinfo):
        super().__init__()
        self.dict_uinfo=dict_uinfo
        # self.window_obj_list.append(self)
        self.root=tkinter.Tk()
        self.show()

    def show(self):
        root=self.root
        root.title("个人资料")
        root.geometry("300x300+100+0")
        uinfo=self.dict_uinfo

        tkinter.Label(root, text="用户名：").grid(row=0, column=0)
        tkinter.Label(root, text=uinfo["uname"]).grid(row=0, column=1)
        tkinter.Label(root, text="年龄：").grid(row=1, column=0)
        tkinter.Label(root, text=uinfo["uage"]).grid(row=1, column=1)

        tkinter.Label(root, text="性别：").grid(row=2, column=0)
        tkinter.Label(root, text=uinfo["usex"]).grid(row=2, column=1)

        tkinter.Label(root, text="地址：").grid(row=3, column=0)
        tkinter.Label(root, text=uinfo["uaddr"]).grid(row=3, column=1)


        root.mainloop()

if __name__ == '__main__':
    uinfo=UserInfo("zs")
    uinfo.show()