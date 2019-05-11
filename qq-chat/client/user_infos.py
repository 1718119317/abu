import tkinter

class UserInfo():
    def __init__(self,name):
        self.uname=name
        self.root=tkinter.Tk()

    def get_info_by_name(self):

        uinfo={"uname":"zs"}
        return uinfo

    def show(self):
        root=self.root
        root.title("个人资料")
        root.geometry("300x300+100+0")
        uinfo=self.get_info_by_name()

        tkinter.Label(root, text="用户名：").grid(row=0, column=0)
        tkinter.Label(root, text=uinfo["uname"]).grid(row=0, column=1)
        tkinter.Label(root, text="年龄：").grid(row=1, column=0)
        tkinter.Label(root, text="性别：").grid(row=2, column=0)
        tkinter.Label(root, text="地址：").grid(row=3, column=0)

        root.mainloop()

if __name__ == '__main__':
    uinfo=UserInfo("zs")
    uinfo.show()