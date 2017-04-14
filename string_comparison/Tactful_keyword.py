import openpyxl
from tkinter import *

wb = openpyxl.load_workbook('block.list.new.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')
def submit():
    b = []
    a = u.get()
    for line in open('queryblock.cs.keyword.txt', 'r', encoding='utf-8'):
        block = line.split('\t')[0]
        if block in a:
            b.append(block)

    if len(b) == 0:
        p.set('没有查询到非法词汇！')
    else:
        p.set(list(set(b)))


root = Tk()
root.title("敏感词查询")

frame = Frame(root)
frame.pack(side=TOP, ipadx=15, pady=10)

lab1 = Label(frame, text="在此输入内容:")
lab1.grid(row=0, column=0, padx=0, pady=0, sticky=W)

#   绑定对象到Entry
u = StringVar()
ent1 = Entry(frame, textvariable=u)
ent1.grid(row=1, column=0, sticky='ew', columnspan=2)

lab2 = Label(frame, text="你的查询结果:")
lab2.grid(row=3, column=0, padx=0, pady=0, sticky=W)

p = StringVar()
ent2 = Entry(frame, textvariable=p)
ent2.grid(row=4, column=0, sticky='ew', columnspan=2)

button = Button(frame, text="开始查询", command=submit, default='active')
button.grid(row=2, column=1, pady=10)


#   以下代码居中显示窗口
root.update_idletasks()
root.geometry("%sx%s+%s+%s" % (500, 350, int((root.winfo_screenwidth() - 500) / 2), int((root.winfo_screenheight() - 300) / 2)))
root.mainloop()
