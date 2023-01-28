import time
from tkinter import*
from tkinter.messagebox import*
root=Tk()
root.geometry('300x200')
root.title("Counter")
hour=StringVar()
minute=StringVar()
second=StringVar()
hour.set("00")
minute.set("00")
second.set("00")
hrs=Entry(root,width=3,font='Broadway 18',textvariable=hour).grid(row=0,column=0)
mins=Entry(root,width=3,font='Broadway 18',textvariable=minute).grid(row=0,column=1)
secs=Entry(root,width=3,font='Broadway 18',textvariable=second).grid(row=0,column=2)
def counter():
    try:
        temp=int(hour.get())*3600+int(minute.get())*60+int(second.get())
    except:
        print("please input right value")
    while temp>-1:
        mints,sec=divmod(temp,60)
        hr=0
        if mints>60:
            hr,mints=divmod(mints,60)
        hour.set("{0:2d}".format(hr))
        minute.set("{0:2d}".format(mints))
        second.set("{0:2d}".format(sec))
        root.update()
        time.sleep(1)
        if temp==0:
            showinfo("countdown","time's up")
        temp=temp-1
Button(root,text="Start",bd=5,command=counter).grid(row=1,column=3)
def reset():
    set.time=0

Button(root,text="reset",bd=5,command=reset).grid(row=2,column=3)
def pause():
    time.sleep(20)   
Button(root,text="Pause",bd='5',command=pause).grid(row=3,column=3)
root.mainloop()
