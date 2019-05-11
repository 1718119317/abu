import tkinter
from tkinter import ttk
# from PIL import Image,ImageTk
class AddFrend():
    def __init__(self):
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

    def search_by_name(self,event):
        res = ["张三", "李四"]
        for item in res:
            tkinter.Label(listbox_show, text=item).pack()
        print(res)

if __name__ == '__main__':
    add=AddFrend()
    add.show()