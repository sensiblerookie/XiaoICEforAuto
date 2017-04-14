# from tkinter import *           # 导入 Tkinter 库
# root = Tk()                     # 创建窗口对象的背景色
# # 创建两个列表
# li = ['C', 'python', 'php', 'html', 'SQL', 'java']
# movie = ['CSS', 'jQuery', 'Bootstrap']
#
# list1 = Listbox(root)           #  创建两个列表组件
# list2 = Listbox(root)
# text = Text(root)
# for item in li:                 # 第一个小部件插入数据
#     list1.insert(0, item)
#
# for item in movie:              # 第二个小部件插入数据
#     list2.insert(0, item)
#
# list1.pack()                    # 将小部件放置到主窗口中
# list2.pack()
#
# root.mainloop()                 # 进入消息循环

# from tkinter import Tk, Text, BOTH, X, N, LEFT, Frame, Label, Entry, Button
#
#
#
# class Example(Frame):
#     def __init__(self, parent):
#         Frame.__init__(self, parent)
#
#         self.parent = parent
#         self.initUI()
#
#     def initUI(self):
#         self.parent.title("敏感词查找")
#         self.pack(fill=BOTH, expand=True)
#
#         frame1 = Frame(self)
#         frame1.pack(fill=X)
#
#         lbl1 = Label(frame1, text="请输入内容：", width=18)
#         lbl1.pack(side=LEFT, padx=5, pady=5)
#
#         frame2 = Frame(self)
#         frame2.pack(fill=BOTH, expand=True)
#
#         entry1 = Entry(frame2)
#         entry1.pack(fill=BOTH, padx=5, pady=5, expand=True)
#
#         frame5 = Frame(self)
#         frame5.pack(fill=BOTH, expand=True)
#
#         button = Button(frame5, text="开始查找")
#         button.pack(side=LEFT, pady=1, padx=1, expand=True)
#
#         frame3 = Frame(self)
#         frame3.pack(fill=BOTH, expand=True)
#
#         lbl3 = Label(frame3, text="包含以下关键词：", width=18)
#         lbl3.pack(side=LEFT, anchor=N, padx=5, pady=5)
#
#         frame4 = Frame(self)
#         frame4.pack(fill=BOTH, expand=True)
#
#         txt = Text(frame4)
#         txt.pack(fill=BOTH, pady=5, padx=5, expand=True)

# def main():
#     root = Tk()
#     root.geometry("%sx%s+%s+%s" % (500, 300, int((root.winfo_screenwidth() - 500) / 2), int((root.winfo_screenheight() - 300) / 2)))
#
#
#     app = Example(root)
#     root.mainloop()



import openpyxl
from tkinter import *

wb = openpyxl.load_workbook('block.list.new.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')

def submit():
    # print(u.get())
    b = []
    for i in range(0, 100):
        a = u.get()
        z = 0
        for line in open('queryblock.cs.keyword.txt', 'r', encoding='utf-8'):
            block = line.split('\t')[0]
            z += 1
            if block in a:
                b.append(block)
    p.set(list(set(b)))
    # print(list(set(b)))
root = Tk()
root.title("非法词汇查询")


frame = Frame(root)
frame.pack(padx=18, pady=8, ipadx=0)

lab1 = Label(frame, text="请输入内容:")
lab1.grid(row=0, column=0, padx=0, pady=0, sticky=W)

#   绑定对象到Entry
u = StringVar()
ent1 = Entry(frame, textvariable=u)
ent1.grid(row=1, column=0, sticky='ew', columnspan=2)

lab2 = Label(frame, text="查询结果:")
lab2.grid(row=3, column=0, padx=0, pady=0, sticky=W)

p = StringVar()
ent2 = Entry(frame, textvariable=p)
ent2.grid(row=4, column=0, sticky='ew', columnspan=2)

lab3 = Label(frame, text="")
lab3.grid(row=5, column=0, sticky=W)

button = Button(frame, text="开始查询", command=submit, default='active')
button.grid(row=2, column=1, padx=15, pady=5)

# button2 = Button(frame, text="退出", command=quit)
# button2.grid(row=6, column=1, padx=15, pady=5)

#   以下代码居中显示窗口
root.update_idletasks()
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
# root.geometry("+%d+%d" % (x, y))
root.geometry("%sx%s+%s+%s" % (500, 300, int((root.winfo_screenwidth() - 500) / 2), int((root.winfo_screenheight() - 300) / 2)))
root.mainloop()
