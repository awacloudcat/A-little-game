from time import *
from tkinter import *
window = Tk()
window.title("A game by playSgappy       ----仅供娱乐")
window.resizable(0,0)
time_start = time() #开始计时
time_end = time()    #结束计时
time_c= time_end - time_start   #运行所花时间
print('time cost', time_c, 's')





def start_lg():
    global startTime
    startTime = localtime().tm_sec
    global lg
    lg = Button(window,text='Stop',command=stop_lg)
    lg.pack()
def stop_lg():
    endTime = localtime().tm_sec
    sec = abs(endTime-startTime)%60
    var1.set('%02s' %(sec))
    lg.destroy()
var1 = StringVar()
lb1 = Label(window,textvariable=var1)
lb1.pack()