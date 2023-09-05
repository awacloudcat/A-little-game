#!/usr/bin/python
# -*- coding: UTF-8 -*-
from tkinter import *
from time import *
#GUI

window = Tk()
window.title("A game by playSgappy       ----仅供娱乐")
window.resizable(0,0)

#窗口位置
width = 700
height = 400
#获取屏幕分辨率
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
#计算让窗口置于屏幕中心
size_geo = '%dx%d+%d+%d' % (width,height,(screenwidth-width)/2,(screenheight-height)/2)
window.geometry(size_geo)

#输出框
t1 = Text(window,width=83,height=28.5)
t1.insert(END,'>>>')
t1.place(x=0,y=0)
t1.config(state='disabled')

#输出框滚动条
sbar1 = Scrollbar(window)
sbar1.place(height=380,x=580,y=0)
sbar1.config(command=t1.yview)
t1.config(yscrollcommand=sbar1.set)

#输入框
e1 = Entry(window)
e1.place(width=580,height=20,x=0,y=380)
e1.focus()

#>>>和发送到输出框
def enter_repost():
    get = e1.get()
    t1.insert(END,get)
    t1.insert(END,'\n>>>')

#定义函数，方便开关读写
def true():
    t1.config(state='normal')
def false():
    t1.config(state='disabled')

#右键菜单
'''def func():
    true()
    t1.insert(END,'*通过右键菜单发送的消息\n>>>')
    false()
menu = tk.Menu(window,tearoff=False)
menu.add_command(label="执行",command=func)
def command(event):
    menu.post(event.x_root,event.y_root)
window.bind("<Button-3>",command)'''

#菜单
def help():
    true()
    t1.insert(END,'暂时还没有帮助哦！\n>>>')
    false()
def feedback():
    true()
    t1.insert(END,'------------------------\n>>>请向作者QQ或邮箱反馈\n>>>QQ：2570043513\n>>>邮箱：2570043513@qq.com\n>>>------------------------\n>>>')
    false()
mainmenu = Menu(window)
menu = Menu(mainmenu,tearoff=False)
menu.add_command(label="帮助",command=help)
menu.add_command(label="反馈",command=feedback)
menu.add_command(label="待更新")
menu.add_separator()
menu.add_command(label="退出程序",command=window.quit)
mainmenu.add_cascade(label="更多...",menu=menu)
window.config(menu=mainmenu)

#右侧信息
Hp = 20
Food = 20
Goldcoin = 20
msg0 = Message(window,text='信息',width=100)
msg1 = Message(window,text='健康度：',width=100)
msg2 = Message(window,text='饱食度：',width=100)
msg3 = Message(window,text='金币：',width=100)
msg4 = Message(window,text=Hp)
msg5 = Message(window,text=Food)
msg6 = Message(window,text=Goldcoin)
msg0.place(x=625,y=0)
msg1.place(x=600,y=20)
msg2.place(x=600,y=40)
msg3.place(x=600,y=60)
msg4.place(x=650,y=20)
msg5.place(x=650,y=40)
msg6.place(x=650,y=60)

#程序运行时间
star=time()
def gettime(): 
    elap = time()-star
    minutes = int(elap/60)
    seconds = int(elap-minutes*60.0)
    var.set('%02d:%02d' %(minutes, seconds))
    window.after(1000,gettime)
var = StringVar()
lb = Label(window,textvariable=var)
lb.place(x=620,y=350)
gettime()

#背包
def open_bag():
    file_bag = open('./data/bag.dat',mode='r+',encoding='UTF-8')
    str_bag = file_bag.read()
    file_bag.close()
    #输出
    t1.insert(END,'你背包里有:' + str_bag + '\n>>>')

#清屏
def clean():
    true()
    t1.delete("1.0","end")
    t1.insert(END,'>>>已执行清屏\n>>>')
    false()

#伐木-未完善
def start_lg():
    t1.insert(END,'已开始计时\n>>>')
    global start_t
    start_t = time()
    global lg
    lg = Button(window,text='Stop',command=stop_lg)
    lg.place(width=80,height=20,x=600,y=300)
def stop_lg():
    stop_t = time()
    t = stop_t - start_t
    t = str(int(t))
    true()
    t1.insert(END,'计时结束,时间为 ' + t + ' s\n>>>')
    false()
    lg.destroy()

#向背包添加物品
all_item = ['原木']
def give():
    get = e1.get()
    list_get = get.split(' ')
    str_item = ''.join(list_get[1])
    if str_item in all_item:
        file_bag = open('./data/bag.dat',mode='a',encoding='UTF-8')
        file_bag.write(str_item)
        file_bag.write(' ')
        file_bag.close()
        t1.insert(END,'获得了 ' + str_item + '\n>>>')
    else:
        t1.insert(END,'物品不存在\n>>>')

#指令识别
def command():
    get = e1.get()
    if '/' in get:
        #以下为指令添加
        if get == '/bag':
            open_bag()
        elif get == '/clean':
            clean()
        elif get == '/lg':
            start_lg()
        elif '/give' in get:
            give()
        else:
            t1.insert(END,'错误：命令不存在\n>>>')

#按键Enter
def on_enter():
    true()
    enter_repost()
    command()
    t1.see(END)
    e1.delete(0,END)
    false()
Enter = Button(window,text='Enter',command=on_enter)
Enter.place(width=120,height=20,x=580,y=380)

#键盘Enter
def on_enter_key(event):
    true()
    enter_repost()
    command()
    t1.see(END)
    e1.delete(0,END)
    false()
e1.bind("<Return>", on_enter_key)

window.mainloop()