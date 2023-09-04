import time
seale = 10
print("执行开始".center(seale+2,"-"))
start = time.perf_counter()
for i in range(seale+1):
    a = "*"*i
    b = "."*(seale-i)
    c = (i/seale)*100
    dur = start = time.perf_counter()-start
    print("\r{:<3.0f}%[{}->{}]{:.2f}s)".format(c,a,b,dur),end="")
    time.sleep(1)