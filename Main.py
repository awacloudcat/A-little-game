#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import tkinter as tk
import time as tt
import json
#GUI

window = tk.Tk()
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

#文本框
t1 = tk.Text(window)
t1.insert(tk.END,'>>>')
t1.place(x=0,y=0,width=580,height=380)
t1.config(state='disabled')

#文本框滚动条
sbar1 = tk.Scrollbar(window)
sbar1.place(height=380,x=580,y=0)
sbar1.config(command=t1.yview)
t1.config(yscrollcommand=sbar1.set)

#输入框
e1 = tk.Entry(window)
e1.place(width=580,height=20,x=0,y=380)
e1.focus()

#>>>和发送到文本框
def enter_repost():
    get = e1.get()
    t1.insert(tk.END,get)
    t1.insert(tk.END,'\n>>>')

#方便开关文本框读写
def true():
    t1.config(state='normal')
def false():
    t1.config(state='disabled')

#右键菜单
def func():
    true()
    t1.insert(tk.END,'*通过右键菜单发送的消息\n>>>')
    false()
menu0 = tk.Menu(window,tearoff=False)
menu0.add_command(label="执行",command=func)
def command(event):
    menu0.post(event.x_root,event.y_root)
window.bind("<Button-3>",command)

#菜单
def help():
    true()
    t1.insert(tk.END,'暂时还没有帮助哦！\n>>>')
    false()
def feedback():
    true()
    t1.insert(tk.END,'------------------------\n>>>请向作者QQ或邮箱反馈\n>>>QQ：2570043513\n>>>邮箱：2570043513@qq.com\n>>>------------------------\n>>>')
    false()
mainmenu = tk.Menu(window)
menu = tk.Menu(mainmenu,tearoff=False)
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
Goldcoin = 1145
msg0 = tk.Message(window,text='信息',width=100)
msg1 = tk.Message(window,text='健康度：',width=100)
msg2 = tk.Message(window,text='饱食度：',width=100)
msg3 = tk.Message(window,text='金币：',width=100)
msg4 = tk.Message(window,text=Hp)
msg5 = tk.Message(window,text=Food)
msg6 = tk.Message(window,text=Goldcoin)
msg0.place(x=625,y=0)
msg1.place(x=600,y=20)
msg2.place(x=600,y=40)
msg3.place(x=600,y=60)
msg4.place(x=650,y=20)
msg5.place(x=650,y=40)
msg6.place(x=650,y=60)

#程序运行时间
star=tt.time()
def gettime(): 
    elap = tt.time()-star
    minutes = int(elap/60)
    seconds = int(elap-minutes*60.0)
    var.set('%02d:%02d' %(minutes, seconds))
    window.after(1000,gettime)
var = tk.StringVar()
lb = tk.Label(window,textvariable=var)
lb.place(x=620,y=350)
gettime()

#背包
def open_bag():
    with open('./data/bag.json',mode='r+',encoding='UTF-8') as f:
        bag = json.dumps(json.load(f),ensure_ascii=False,indent=4,separators=(', ', ': '))
    #输出
    t1.insert(tk.END,'你背包里有:' + bag + '\n>>>')

#清屏
def clear():
    t1.delete("1.0","end")
    t1.insert(tk.END,'>>>已执行清屏\n>>>')

#给予物品（指令）
all_item = [
    '木头','石头',
    '铁','金',
    '小麦种子','水稻种子','土豆种子'
]
def get():
    get = e1.get()
    list_get = get.split(' ')
    item = ''.join(list_get[1])
    qty = ''.join(list_get[2])
    if item in all_item:
        with open('data\\bag.json',mode='r',encoding='UTF-8') as r_f:
            bag = json.load(r_f)
            r_f.close()
            if item not in bag:
                bag[item] = int(qty)
            else:
                bag[item] = bag[item] + int(qty)
        with open("data\\bag.json",'w',encoding='utf-8') as w_f:
            json.dump(bag,w_f,ensure_ascii=False,indent=4,separators=(', ', ': '))
            w_f.close()
        t1.insert(tk.END,'获得了 '+ qty + ' 个 ' + item + '\n>>>')
    else:
        t1.insert(tk.END,'物品不存在\n>>>')
#（机制）
def give(item,qty):
    if item in all_item:
        with open('data\\bag.json',mode='r',encoding='UTF-8') as r_f:
            bag = json.load(r_f)
            r_f.close()
            if item not in bag:
                bag[item] = int(qty)
            else:
                bag[item] = bag[item] + int(float(qty))
        with open("data\\bag.json",'w',encoding='utf-8') as w_f:
            json.dump(bag,w_f,ensure_ascii=False,indent=4,separators=(', ', ': '))
            w_f.close()
        t1.insert(tk.END,'获得了 '+ qty + ' 个 ' + item + '\n>>>')

#伐木
def start_lg():
    t1.insert(tk.END,'已开始伐木,右下角结束伐木\n>>>')
    global start_t
    global lg
    start_t = tt.time()
    lg = tk.Button(window,text='结束伐木',command=stop_lg)
    lg.place(width=80,height=20,x=600,y=300)
def stop_lg():
    stop_t = tt.time()
    t = stop_t - start_t
    w = str(int(int(t) / 1))
    t = str(int(t))
    give('木头',w)
    true()
    t1.insert(tk.END,'伐木结束,时间为' + t + 's,共获得木头' + w + '个\n>>>')
    false()
    lg.destroy()

#指令识别
def command():
    getting = e1.get()
    if '/' in getting:
        #以下为指令添加
        if getting == '/bag':
            open_bag()
        elif getting == '/clear':
            clear()
        elif getting == '/lg':
            start_lg()
        elif '/get' in getting:
            if getting == '/get':
                t1.insert(tk.END,'Error:命令不完整\n>>>')
            else:
                get()
        else:
            t1.insert(tk.END,'Error:命令不存在\n>>>')

#按键Enter
def enter():
    true()
    enter_repost()
    command()
    t1.see(tk.END)
    e1.delete(0,tk.END)
    false()
Enter = tk.Button(window,text='Enter',command=enter)
Enter.place(width=120,height=20,x=580,y=380)

#键盘Enter
def enter_key(event):
    true()
    enter_repost()
    command()
    t1.see(tk.END)
    e1.delete(0,tk.END)
    false()
e1.bind("<Return>", enter_key)

window.mainloop()