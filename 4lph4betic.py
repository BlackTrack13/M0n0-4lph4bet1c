import string
import random
import sys
import BK_Tools
import tkinter as tk
from tkinter import *
txt = ""
shuf = 0
encrypted=[]

setter1 = -210
setter2 = 510
setter3 = 80
setter4 = 210

frm = tk.Tk()
frm.geometry('700x910')
BK_Tools.tkcenter(frm)
frm.config(bg="#240C39")
frm.title("M0n04lph4betic")


A = 'abcdefghijklmnopqrstuvwxyz'.split()
B = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
k3y = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']






a = tk.Label(frm, font=("Minecraftia", 11), text="A", width=3, height=1, bg="black", fg="white")
a.place(x=610, y=1)
b = tk.Label(frm, font=("Minecraftia", 11), text="B", width=3, height=1, bg="white", fg="black")
b.place(x=610, y=35)
c = tk.Label(frm, font=("Minecraftia", 11), text="C", width=3, height=1, bg="black", fg="white")
c.place(x=610, y=70)
d = tk.Label(frm, font=("Minecraftia", 11), text="D", width=3, height=1, bg="white", fg="black")
d.place(x=610, y=105)
e = tk.Label(frm, font=("Minecraftia", 11), text="E", width=3, height=1, bg="black", fg="white")
e.place(x=610, y=140)
aX = tk.Label(frm, font=("Minecraftia", 11), text=k3y[0], width=3, height=1, bg="black", fg="white")
aX.place(x=660, y=1)
bX = tk.Label(frm, font=("Minecraftia", 11), text=k3y[1], width=3, height=1, bg="white", fg="black")
bX.place(x=660, y=35)
cX = tk.Label(frm, font=("Minecraftia", 11), text=k3y[2], width=3, height=1, bg="black", fg="white")
cX.place(x=660, y=70)
dX = tk.Label(frm, font=("Minecraftia", 11), text=k3y[3], width=3, height=1, bg="white", fg="black")
dX.place(x=660, y=105)
eX = tk.Label(frm, font=("Minecraftia", 11), text=k3y[4], width=3, height=1, bg="black", fg="white")
eX.place(x=660, y=140)
#==
f = tk.Label(frm, font=("Minecraftia", 11), text="F", width=3, height=1, bg="white", fg="black")
f.place(x=610, y=175)
g = tk.Label(frm, font=("Minecraftia", 11), text="G", width=3, height=1, bg="black", fg="white")
g.place(x=610, y=210)
h = tk.Label(frm, font=("Minecraftia", 11), text="H", width=3, height=1, bg="white", fg="black")
h.place(x=610, y=245)
i = tk.Label(frm, font=("Minecraftia", 11), text="I", width=3, height=1, bg="black", fg="white")
i.place(x=610, y=280)
j = tk.Label(frm, font=("Minecraftia", 11), text="J", width=3, height=1, bg="white", fg="black")
j.place(x=610, y=315)
fX = tk.Label(frm, font=("Minecraftia", 11), text=k3y[5], width=3, height=1, bg="white", fg="black")
fX.place(x=660, y=175)
gX = tk.Label(frm, font=("Minecraftia", 11), text=k3y[6], width=3, height=1, bg="black", fg="white")
gX.place(x=660, y=210)
hX = tk.Label(frm, font=("Minecraftia", 11), text=k3y[7], width=3, height=1, bg="white", fg="black")
hX.place(x=660, y=245)
iX = tk.Label(frm, font=("Minecraftia", 11), text=k3y[8], width=3, height=1, bg="black", fg="white")
iX.place(x=660, y=280)
jX = tk.Label(frm, font=("Minecraftia", 11), text=k3y[9], width=3, height=1, bg="white", fg="black")
jX.place(x=660, y=315)
#==
k = tk.Label(frm, font=("Minecraftia", 11), text="K", width=3, height=1, bg="black", fg="white")
k.place(x=610, y=350)
l = tk.Label(frm, font=("Minecraftia", 11), text="L", width=3, height=1, bg="white", fg="black")
l.place(x=610, y=385)
m = tk.Label(frm, font=("Minecraftia", 11), text="M", width=3, height=1, bg="black", fg="white")
m.place(x=610, y=420)
n = tk.Label(frm, font=("Minecraftia", 11), text="N", width=3, height=1, bg="white", fg="black")
n.place(x=610, y=455)
o = tk.Label(frm, font=("Minecraftia", 11), text="O", width=3, height=1, bg="black", fg="white")
o.place(x=610, y=490)
kX = tk.Label(frm, font=("Minecraftia", 11), text=k3y[10], width=3, height=1, bg="black", fg="white")
kX.place(x=660, y=350)
lX = tk.Label(frm, font=("Minecraftia", 11), text=k3y[11], width=3, height=1, bg="white", fg="black")
lX.place(x=660, y=385)
mX = tk.Label(frm, font=("Minecraftia", 11), text=k3y[12], width=3, height=1, bg="black", fg="white")
mX.place(x=660, y=420)
nX = tk.Label(frm, font=("Minecraftia", 11), text=k3y[13], width=3, height=1, bg="white", fg="black")
nX.place(x=660, y=455)
oX = tk.Label(frm, font=("Minecraftia", 11), text=k3y[14], width=3, height=1, bg="black", fg="white")
oX.place(x=660, y=490)
#=1
p = tk.Label(frm, font=("Minecraftia", 11), text="P", width=3, height=1, bg="white", fg="black")
p.place(x=610, y=525)
q = tk.Label(frm, font=("Minecraftia", 11), text="Q", width=3, height=1, bg="black", fg="white")
q.place(x=610, y=560)
r = tk.Label(frm, font=("Minecraftia", 11), text="R", width=3, height=1, bg="white", fg="black")
r.place(x=610, y=595)
s = tk.Label(frm, font=("Minecraftia", 11), text="S", width=3, height=1, bg="black", fg="white")
s.place(x=610, y=630)
t = tk.Label(frm, font=("Minecraftia", 11), text="T", width=3, height=1, bg="white", fg="black")
t.place(x=610, y=665)
pX = tk.Label(frm, font=("Minecraftia", 11), text=k3y[15], width=3, height=1, bg="white", fg="black")
pX.place(x=660, y=525)
qX = tk.Label(frm, font=("Minecraftia", 11), text=k3y[16], width=3, height=1, bg="black", fg="white")
qX.place(x=660, y=560)
rX = tk.Label(frm, font=("Minecraftia", 11), text=k3y[17], width=3, height=1, bg="white", fg="black")
rX.place(x=660, y=595)
sX = tk.Label(frm, font=("Minecraftia", 11), text=k3y[18], width=3, height=1, bg="black", fg="white")
sX.place(x=660, y=630)
tX = tk.Label(frm, font=("Minecraftia", 11), text=k3y[19], width=3, height=1, bg="white", fg="black")
tX.place(x=660, y=665)
#==
u = tk.Label(frm, font=("Minecraftia", 11), text="U", width=3, height=1, bg="black", fg="white")
u.place(x=610, y=700)
v = tk.Label(frm, font=("Minecraftia", 11), text="V", width=3, height=1, bg="white", fg="black")
v.place(x=610, y=735)
w = tk.Label(frm, font=("Minecraftia", 11), text="W", width=3, height=1, bg="black", fg="white")
w.place(x=610, y=770)
x = tk.Label(frm, font=("Minecraftia", 11), text="X", width=3, height=1, bg="white", fg="black")
x.place(x=610, y=805)
y = tk.Label(frm, font=("Minecraftia", 11), text="Y", width=3, height=1, bg="black", fg="white")
y.place(x=610, y=840)
z = tk.Label(frm, font=("Minecraftia", 11), text="Z", width=3, height=1, bg="white", fg="black")
z.place(x=610, y=875)
uX = tk.Label(frm, font=("Minecraftia", 11), text=k3y[20], width=3, height=1, bg="black", fg="white")
uX.place(x=660, y=700)
vX = tk.Label(frm, font=("Minecraftia", 11), text=k3y[21], width=3, height=1, bg="white", fg="black")
vX.place(x=660, y=735)
wX = tk.Label(frm, font=("Minecraftia", 11), text=k3y[22], width=3, height=1, bg="black", fg="white")
wX.place(x=660, y=770)
xX = tk.Label(frm, font=("Minecraftia", 11), text=k3y[23], width=3, height=1, bg="white", fg="black")
xX.place(x=660, y=805)
yX = tk.Label(frm, font=("Minecraftia", 11), text=k3y[24], width=3, height=1, bg="black", fg="white")
yX.place(x=660, y=840)
zX = tk.Label(frm, font=("Minecraftia", 11), text=k3y[25], width=3, height=1, bg="white", fg="black")
zX.place(x=660, y=875)





def input():
    global txt
    txt = textarea.get()

def shuffle():
    global arr
    global shuf
    shuf += 1
    def on():

        k = "zyxwvutsrqponmlkjihgfedcba"
        #k = "qokxatfimzelcrpbygvnsujhwd"
        k3y = []
        for i in k:
            k3y.append(i)


        aX["text"] =k3y[0]
        bX["text"] =k3y[1]
        cX["text"] =k3y[2]
        dX["text"] =k3y[3]
        eX["text"] =k3y[4]
        fX["text"] =k3y[5]
        gX["text"] =k3y[6]
        hX["text"] =k3y[7]
        iX["text"] =k3y[8]
        jX["text"] =k3y[9]
        kX["text"] =k3y[10]
        lX["text"] =k3y[11]
        mX["text"] =k3y[12]
        nX["text"] =k3y[13]
        oX["text"] =k3y[14]
        pX["text"] =k3y[15]
        qX["text"] =k3y[16]
        rX["text"] =k3y[17]
        sX["text"] =k3y[18]
        tX["text"] =k3y[19]
        uX["text"] =k3y[20]
        vX["text"] =k3y[21]
        wX["text"] =k3y[22]
        xX["text"] =k3y[23]
        yX["text"] =k3y[24]
        zX["text"] =k3y[25]

    def off():

        k3y=[]
        kk = "pilmxtzugbkoqrsvcyjfhdwean"

        for i in kk:
            k3y.append(i)

        aX["text"] =k3y[0]
        bX["text"] =k3y[1]
        cX["text"] =k3y[2]
        dX["text"] =k3y[3]
        eX["text"] =k3y[4]
        fX["text"] =k3y[5]
        gX["text"] =k3y[6]
        hX["text"] =k3y[7]
        iX["text"] =k3y[8]
        jX["text"] =k3y[9]
        kX["text"] =k3y[10]
        lX["text"] =k3y[11]
        mX["text"] =k3y[12]
        nX["text"] =k3y[13]
        oX["text"] =k3y[14]
        pX["text"] =k3y[15]
        qX["text"] =k3y[16]
        rX["text"] =k3y[17]
        sX["text"] =k3y[18]
        tX["text"] =k3y[19]
        uX["text"] =k3y[20]
        vX["text"] =k3y[21]
        wX["text"] =k3y[22]
        xX["text"] =k3y[23]
        yX["text"] =k3y[24]
        zX["text"] =k3y[25]




    if shuf % 2 == 0:
        on()

    else :
        off()



arr={ 'a':k3y[0],
      'b':k3y[1],
      'c':k3y[2],
      'd':k3y[3],
      'e':k3y[4],
      'f':k3y[5],
      'g':k3y[6],
      'h':k3y[7],
      'i':k3y[8],
      'j':k3y[9],
      'k':k3y[10],
      'l':k3y[11],
      'm':k3y[12],
      'n':k3y[13],
      'o':k3y[14],
      'p':k3y[15],
      'q':k3y[16],
      'r':k3y[17],
      's':k3y[18],
      't':k3y[19],
      'u':k3y[20],
      'v':k3y[21],
      'w':k3y[22],
      'x':k3y[23],
      'y':k3y[24],
      'z':k3y[25],
     }

arr2={'a':"p",
      'b':"i",
      'c':"l",
      'd':"m",
      'e':"x",
      'f':"t",
      'g':"z",
      'h':"u",
      'i':"g",
      'j':"b",
      'k':"k",
      'l':"o",       #"pilmxtzugbkoqrsvcyjfhdwean"
      'm':"q",
      'n':"r",
      'o':"s",
      'p':"v",
      'q':"c",
      'r':"y",
      's':"j",
      't':"f",
      'u':"h",
      'v':"d",
      'w':"w",
      'x':"e",
      'y':"a",
      'z':"n",
     }

reverse_keys2 = {}
for k3y, index in arr2.items():
    reverse_keys2[index] = k3y



reverse_keys = {}
for k3y, index in arr.items():
    reverse_keys[index] = k3y

def path1():
    global new
    global txt
    global encrypted
    TXT = txt.upper()
    new =[]
    for X in TXT:
        new += X

    black =[aX,cX,eX,gX,iX,kX,mX,oX,qX,sX,uX,wX,yX]
    for bb in black:
        bb.config(bg='black',fg="white")
    white =[bX,dX,fX,hX,jX,lX,nX,pX,rX,tX,vX,xX,zX]
    for ww in white:
        ww.config(bg='white',fg="black")

    for item in frm.winfo_children():
        for i in range(len(txt)):
            if item.cget("text") == new[i]:
                item.config(bg='red',fg="white")
            if item.cget("text") == encrypted[i]:
                item.config(bg='green',fg="white")

def clear():
    text.delete('1.0', END)
    f = open('S0urce.txt', 'r+')
    f.truncate(0)
    unpath()

def log():
    f = open("S0urce.txt", "r")
    text.delete('1.0',END)
    text.insert('1.0', f.readlines())

open_button = tk.Button(frm,text='Clear',font=("Vermin Vibes 1989",15 ),fg='orange', pady=8,bg='#222222',command =lambda :[clear()])
text = tk.Text(frm, height=9,width=50,bg="black",fg="#24E53E",state=NORMAL,font=("Courier New",10 ))
open_button.place(x=110, y=850)
text.place(x=110, y=700)

def Encrypt():
    input()

    global txt
    global arr
    global encrypted
    global shuf

    str(txt)
    encrypted = []
    if shuf % 2 ==0:
        for l in txt:
            encrypted.append(arr.get(l,l))
        print(''.join(encrypted))
        print(txt+"-->")
        print(encrypted)
        print("-=-=-=-=-Enc=sh1-=-=-=-=-=|")
    else:
        for l in txt:
            encrypted.append(arr2.get(l,l))
        print(''.join(encrypted))
        print(txt+"-->")
        print(encrypted)
        print("-=-=-=-=-Enc=sh2-=-=-=-=-=|")
    Ec["state"] = DISABLED
    Dc["state"] = NORMAL
    result.config(font=("Minecraftia", 17))
    result.config(text=encrypted)

    result.place(x=270, y=365)
    panel.config(image=pp)
    path1()



def unpath():


    black =[a,c,e,g,i,k,m,o,q,s,u,w,y,aX,cX,eX,gX,iX,kX,mX,oX,qX,sX,uX,wX,yX]
    for bb in black:
        bb.config(bg='black',fg="white")
    white =[b,d,f,h,j,l,n,p,r,t,v,x,z,bX,dX,fX,hX,jX,lX,nX,pX,rX,tX,vX,xX,zX]
    for ww in white:
        ww.config(bg='white',fg="black")



def Decrypt():
    input()
    global key
    global encrypted
    global shuf

    str(encrypted)
    decrypted=[]

    if shuf % 2 ==0:
        for l in encrypted:
            decrypted.append(reverse_keys.get(l,l))
        print(''.join(decrypted))
        print(txt+"-->")
        print(decrypted)
        print("-=-=-=-=-Dec=sh1-=-=-=-=-=|")
    else:
        for l in encrypted:
            decrypted.append(reverse_keys2.get(l,l))
        print(''.join(decrypted))
        print(txt+"-->")
        print(decrypted)
        print("-=-=-=-=-Dec=sh2-=-=-=-=-=|")
    Dc["state"] = DISABLED
    Ec["state"] = NORMAL
    result.config(font=("Minecraftia", 17))
    result.config(text=decrypted)
    result.place(x=270, y=365)
    panel.config(image=pp2)
    unpath()
    writer = open("S0urce.txt", "a")
    writer.write(txt+"<--()-->"+str(encrypted)+"\n")
    writer.close()
    log()




def dec():
    global setter4
    if setter4 <= 510 :
        setter4 += 5
        Dc.place(x=240 ,y=setter4)# Dc.place(x=240,y=510)
        frm.after(20, dec)
        frm.update()
        if setter4 == 510:
            Sh.place(x=490, y=280)



def set2PosYE():
    global setter3
    if setter3 != 210 :
        setter3 += 5
        Ec.place(x=240 ,y=setter3)#Ec.place(x=240,y=210)


        frm.after(50, set2PosYE)
        frm.update()
        if setter3 == 210 :
            dec()



def set1PosYE():
    global setter1
    if setter1 <= 50 :
        setter1 += 2
        panel.place(x=setter1 ,y=70)#x=120,y=210

        frm.after(10, set1PosYE)
        frm.update()
        if setter1 == 1120:
            Ec["state"] = NORMAL





open_button = tk.Button(frm,text='Clear',font=("Vermin Vibes 1989",15 ),fg='#24E53E', pady=8,bg='#222222',command =lambda :[clear()])

line1 = Canvas(frm,width=3,height=900,bg='white',relief=RAISED)
#line1.place(x=100,y=300)



pp = PhotoImage(file='lvl1.png')
pp2 = PhotoImage(file='lvl2.png')

panel = tk.Label(frm,image = pp,bg="#240C39",bd=10,)
#panel.place(x=110, y=80)
textarea = tk.Entry(frm, width=20, font=("Arial", 18), borderwidth=3, relief="groove",
                 highlightcolor="white",bg='#222222',fg="white")
textarea.place(x=182,y=120)

Sh = tk.Button(frm, text="S\nh\nu\nf\nf\nl\ne",font=("Vermin Vibes 1989",22 ),fg='yellow', pady=8,bg='#222222',command = shuffle)


Ec = tk.Button(frm, text="Encrypt",font=("Vermin Vibes 1989",22 ),fg='red', pady=8,bg='#222222', command =Encrypt)
#Ec.place(x=240,y=210)
#Ec.bind("<Button-1>", path)


Dc = tk.Button(frm, text="Decrypt",font=("Vermin Vibes 1989",22 ),fg='#24E53E', pady=8,bg='#222222',command =Decrypt)
#Dc.place(x=240,y=510)
mainT = tk.Label(frm, text="Mono Alphabetic", font=("Metal Gear", 40),fg="white",bg="#240c39",justify='center' )
mainT.place(x=15,y=0)
set1PosYE()

set2PosYE()
Dc["state"] = DISABLED

result = tk.Label(frm,font=("Minecraftia", 24),bg="#140620",fg="white" )

frm.mainloop()