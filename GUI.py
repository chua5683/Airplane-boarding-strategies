from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter.ttk import *
import time
import Airline3v
import Airline3
import Ordering
import random
import math
import numpy
from random import randrange, sample
def random_insert(lst, item):
    lst.insert(randrange(len(lst)+1), item)
    return lst


window = Tk()
window.title("Get Ready to board a plane!")
window.configure(background="gray")
window.geometry('1000x500')

lblscheme = Label(window, text="Choose a Boarding Scheme")
lblscheme.grid(column=0, row=0)
combo = Combobox(window)
combo['values']= ('BTF', 'BLOCK','WILMA', 'RASS', 'RFOALL', 'STFOPT','STFMOD','Amigos')
combo.current(0) #set the selected item
combo.grid(column=1, row=0)
lblrow = Label(window, text="Number of Rows")
lblrow.grid(column=0, row=1)
txtrow = Entry(window,width=4)
txtrow.insert(END,30)
txtrow.grid(column=1, row=1)
lblcol = Label(window, text="Number of Columns")
lblcol.grid(column=0, row=2)
txtcol = Entry(window,width=4)
txtcol.insert(END,6)
txtcol.grid(column=1, row=2)
lblgroup = Label(window, text="Number of Groups")
lblgroup.grid(column=0, row=3)
txtgroup = Entry(window,width=4)
txtgroup.insert(END,3)
txtgroup.grid(column=1, row=3)

lblbag = Label(window, text="Percent of passengers with bags")
lblbag.grid(column=0, row=4)
txtbag = Entry(window,width=4)
txtbag.insert(END,80)
txtbag.grid(column=1, row=4)

v1 = IntVar()
v2 = IntVar()
bagrad1 = Radiobutton(window,text='Distribution bag loading', value=1,variable=v1)
bagrad2 = Radiobutton(window,text='Same', value=2,variable=v1)
v1.set(1)
v2.set(3)
bagrad1.grid(column=0, row=5)
bagrad2.grid(column=4, row=5)
lblbagm = Label(window, text="Mean")
lblbagm.grid(column=0, row=6)
txtbagm = Entry(window,width=4)
txtbagm.insert(END,12)
txtbagm.grid(column=1, row=6)
lblbagsd = Label(window, text="s.d.")
lblbagsd.grid(column=2, row=6)
txtbagsd = Entry(window,width=4)
txtbagsd.insert(END,2)
txtbagsd.grid(column=3, row=6)
lblbagc = Label(window, text="Bagtime")
lblbagc.grid(column=4, row=6)
txtbagc = Entry(window,width=4)
txtbagc.insert(END,12)
txtbagc.grid(column=5, row=6)

speedrad1 = Radiobutton(window,text='Distribution for walk speeds', value=3,variable=v2)
speedrad2 = Radiobutton(window,text='Same', value=4,variable=v2)
speedrad1.grid(column=0, row=7)
speedrad2.grid(column=4, row=7)
lblspm = Label(window, text="Mean")
lblspm.grid(column=0, row=8)
txtspm = Entry(window,width=4)
txtspm.insert(END,1.5)
txtspm.grid(column=1, row=8)
lblspsd = Label(window, text="s.d.")
lblspsd.grid(column=2, row=8)
txtspsd = Entry(window,width=4)
txtspsd.insert(END,.3)
txtspsd.grid(column=3, row=8)
lblspc = Label(window, text="Speed")
lblspc.grid(column=4, row=8)
txtspc = Entry(window,width=4)
txtspc.insert(END,1.5)
txtspc.grid(column=5, row=8)

lblstep = Label(window, text="Step Size")
lblstep.grid(column=0, row=9)
txtstep = Entry(window,width=4)
txtstep.insert(END,.5)
txtstep.grid(column=1, row=9)
lblspeed = Label(window, text="Animation speed")
lblspeed.grid(column=0, row=10)
txtspeed = Entry(window,width=4)
txtspeed.insert(END,.01)
txtspeed.grid(column=1, row=10)

lblps = Label(window, text="Personal space")
lblps.grid(column=0, row=11)
txtps = Entry(window,width=3)
txtps.insert(END,.7)
txtps.grid(column=1, row=11)
lblctpp = Label(window, text="Time to climb per person")
lblctpp.grid(column=0, row=12)
txtctpp = Entry(window,width=3)
txtctpp.insert(END,6)
txtctpp.grid(column=1, row=12)
lblsn = Label(window, text="Space needed to load bag")
lblsn.grid(column=0, row=13)
txtsn = Entry(window,width=3)
txtsn.insert(END,1)
txtsn.grid(column=1, row=13)

lblpb = Label(window, text="Percent of passengers pre-boarded")
lblpb.grid(column=3, row=3)
txtpb = Entry(window,width=3)
txtpb.insert(END,0)
txtpb.grid(column=4, row=3)

lblwo = Label(window, text="Percent of passengers out of order")
lblwo.grid(column=3, row=4)
txtwo = Entry(window,width=3)
txtwo.insert(END,0)
txtwo.grid(column=4, row=4)

def clicked():
    seatlist=Ordering.ordering(int(txtrow.get()),int(txtcol.get()),int(txtgroup.get()),combo.get())
    if int(txtpb.get())>0:
        pb=int(math.ceil(int(txtpb.get())/100*len(seatlist)))
        pbList=[]
        for i in range(pb):
            pbList.append(seatlist.pop(random.randint(0,len(seatlist)-1)))
        seatlist=pbList+seatlist

    if int(txtwo.get())>0:
        wo=int(math.ceil(int(txtwo.get())/100*len(seatlist)))
        woList=[]
        for i in range(wo):
            woList.append(seatlist.pop(random.randint(0,len(seatlist)-1)))
        for i in range(wo):
            seatlist=random_insert(seatlist,woList[i])
            

    if v1.get()==1:
        numbags=int(math.ceil(len(seatlist)*float(txtbag.get())/100))
        blist=list(numpy.random.normal(float(txtbagm.get()),float(txtbagsd.get()),numbags))+[0 for i in range(len(seatlist)-numbags)]
        random.shuffle(blist)
    else:
        numbags=int(math.ceil(len(seatlist)*float(txtbag.get())/100))
        blist=[float(txtbagc.get()) for i in range(numbags)]+[0 for i in range(len(seatlist)-numbags)]
        random.shuffle(blist)
    if v2.get()==3:
        speedlist=list(numpy.random.normal(float(txtspm.get()),float(txtspsd.get()),len(seatlist)))
        random.shuffle(blist)
    else:
        speedlist=[float(txtspc.get()) for i in range(len(seatlist))]
    Airline3v.visualboard(seatlist,float(txtstep.get()),float(txtspeed.get()),float(txtps.get()),float(txtctpp.get()),float(txtsn.get()),speedlist,blist)

def clicked1():
    seatlist=Ordering.ordering(int(txtrow.get()),int(txtcol.get()),int(txtgroup.get()),combo.get())
    if int(txtpb.get())>0:
        pb=int(math.ceil(int(txtpb.get())/100*len(seatlist)))
        pbList=[]
        for i in range(pb):
            pbList.append(seatlist.pop(random.randint(0,len(seatlist)-1)))
        seatlist=pbList+seatlist


    if int(txtwo.get())>0:
        wo=int(math.ceil(int(txtwo.get())/100*len(seatlist)))
        woList=[]
        for i in range(wo):
            woList.append(seatlist.pop(random.randint(0,len(seatlist)-1)))
        for i in range(wo):
            seatlist=random_insert(seatlist,woList[i])
            
        
    if v1.get()==1:
        numbags=int(math.ceil(len(seatlist)*float(txtbag.get())/100))
        blist=list(numpy.random.normal(float(txtbagm.get()),float(txtbagsd.get()),numbags))+[0 for i in range(len(seatlist)-numbags)]
        random.shuffle(blist)
    else:
        numbags=int(math.ceil(len(seatlist)*float(txtbag.get())/100))
        blist=[float(txtbagc.get()) for i in range(numbags)]+[0 for i in range(len(seatlist)-numbags)]
        random.shuffle(blist)
    if v2.get()==3:
        speedlist=list(numpy.random.normal(float(txtspm.get()),float(txtspsd.get()),len(seatlist)))
        random.shuffle(blist)
    else:
        speedlist=[float(txtspc.get()) for i in range(len(seatlist))]
    time=Airline3.board(seatlist,float(txtstep.get()),float(txtps.get()),float(txtctpp.get()),float(txtsn.get()),speedlist,blist)
    res = "Time= " + str(time)
    lbltime.configure(text= res)
def clicked2():
    timelist=[]
    for i in range(int(txtruns.get())):
        seatlist=Ordering.ordering(int(txtrow.get()),int(txtcol.get()),int(txtgroup.get()),combo.get())
        if int(txtpb.get())>0:
            pb=int(math.ceil(int(txtpb.get())/100*len(seatlist)))
            pbList=[]
            for i in range(pb):
                pbList.append(seatlist.pop(random.randint(0,len(seatlist)-1)))
            seatlist=pbList+seatlist

        if int(txtwo.get())>0:
            wo=int(math.ceil(int(txtwo.get())/100*len(seatlist)))
            woList=[]
            for i in range(wo):
                woList.append(seatlist.pop(random.randint(0,len(seatlist)-1)))
            for i in range(wo):
                seatlist=random_insert(seatlist,woList[i])
                
        if v1.get()==1:
            numbags=int(math.ceil(len(seatlist)*float(txtbag.get())/100))
            blist=list(numpy.random.normal(float(txtbagm.get()),float(txtbagsd.get()),numbags))+[0 for i in range(len(seatlist)-numbags)]
            random.shuffle(blist)
        else:
            numbags=int(math.ceil(len(seatlist)*float(txtbag.get())/100))
            blist=[float(txtbagc.get()) for i in range(numbags)]+[0 for i in range(len(seatlist)-numbags)]
            random.shuffle(blist)
        if v2.get()==3:
            speedlist=list(numpy.random.normal(float(txtspm.get()),float(txtspsd.get()),len(seatlist)))
            random.shuffle(blist)
        else:
            speedlist=[float(txtspc.get()) for i in range(len(seatlist))]
        t=Airline3.board(seatlist,float(txtstep.get()),float(txtps.get()),float(txtctpp.get()),float(txtsn.get()),speedlist,blist)
        timelist.append(t)
    #        bar['value'] = ((i+1)/int(txtruns.get()))*100
    #        time.sleep(.01)
    if chk_state.get():
        numpy.savetxt(txtdata.get(), timelist, delimiter=',')


btn = Button(window, text="Visualize Boarding", command=clicked)
btn.grid(column=6, row=11)

btn1 = Button(window, text="Time Boarding", command=clicked1)
btn1.grid(column=6, row=12)

lbltime = Label(window, text="Time=")
lbltime.grid(column=6, row=13)

btn2 = Button(window, text="Multiple Runs", command=clicked2)
btn2.grid(column=1, row=14)
lblruns = Label(window, text="Number of Runs")
lblruns.grid(column=2, row=14)
txtruns = Entry(window,width=5)
txtruns.insert(END,50)
txtruns.grid(column=3, row=14)

#style = ttk.Style()
#style.theme_use('default')
#style.configure("black.Horizontal.TProgressbar", background='black')
#bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
#bar['value'] = 0
#bar.grid(column=2, row=16)

chk_state = BooleanVar()
chk_state.set(True) #set check state
chk = Checkbutton(window, text='save data to file?', var=chk_state)
chk.grid(column=1, row=15)
lbldata = Label(window, text="File Name")
lbldata.grid(column=2, row=15)
txtdata = Entry(window,width=10)
txtdata.insert(END,'data.csv')
txtdata.grid(column=3, row=15)
window.mainloop()
