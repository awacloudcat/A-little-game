from time import *
from tkinter import *
window = Tk()
window.title("A game by playSgappy       ----仅供娱乐")
window.resizable(0,0)
time_start = time() #开始计时
time_end = time()    #结束计时
time_c= time_end - time_start   #运行所花时间
print('time cost', time_c, 's')
import tkinter as tk

root = tk.Tk()

text = tk.Text(root, width=30)
text.pack()

long_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam vitae leo varius, vestibulum risus id, faucibus mauris."
text.insert(tk.END, long_text)

root.mainloop()
