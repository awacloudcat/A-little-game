import time as tt
import tkinter as tk
import json
window = tk.Tk()
width = 700
height = 400
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
size_geo = '%dx%d+%d+%d' % (width,height,(screenwidth-width)/2,(screenheight-height)/2)
window.geometry(size_geo)
window.title("A game by playSgappy       ----仅供娱乐")
window.resizable(0,0)
t1 = tk.Text(window)
t1.insert(tk.END,'>>>')
t1.place(x=0,y=0,width=580,height=380)
e1 = tk.Entry(window)
e1.place(width=580,height=20,x=0,y=380)
e1.focus()


def open_bag():
    with open('./data/bag.json',mode='r+',encoding='UTF-8') as f:
        bag = json.dumps(json.load(f),ensure_ascii=False,indent=4,separators=(', ', ': '))
        #输出
        t1.insert(tk.END,'你背包里有:' + bag + '\n>>>')


item = '木头'
qty = 1
with open('data\\bag.json',mode='r',encoding='UTF-8') as r_f:
            bag = json.load(r_f)
            r_f.close()
            bag[item] = bag[item] + int(qty)
with open("data\\bag.json",'w',encoding='utf-8') as w_f:
            json.dump(bag,w_f,ensure_ascii=False,indent=4,separators=(', ', ': '))
            w_f.close()
t1.insert(tk.END,'获得了 '+ qty + ' 个 ' + item + '\n>>>')

#指令识别
def command():
    getting = e1.get()
    if '/' in getting:
        #以下为指令添加
        if getting == '/bag':
            open_bag()
        else:
            t1.insert(tk.END,'错误：命令不存在\n>>>')
            
def enter_repost():
    get = e1.get()
    t1.insert(tk.END,get)
    t1.insert(tk.END,'\n>>>')

def enter():
    enter_repost()
    command()
    t1.see(tk.END)
    e1.delete(0,tk.END)
Enter = tk.Button(window,text='Enter',command=enter)
Enter.place(width=120,height=20,x=580,y=380)

def enter_key(event):
    enter_repost()
    t1.see(tk.END)
    e1.delete(0,tk.END)
e1.bind("<Return>", enter_key)
window.mainloop()