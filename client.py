from tkinter import *
from tkinter import ttk
import socket
import os

s=0
port=0
soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
l=["chmod","sudo","install","dd","lscpu","lshw","hwinfo","lspci","lsuci","lsusb","lsblk","df","fdisk","mount","free","traceroute","dig","telnet","w","nmap","ifup","ifdown","scp","ls -la"]

def checksum(st):
    return reduce(lambda x,y:x+y, map(ord, st))

class sta():
    def __init__(self):
        self.window = Tk()
        self.window.title("Login")
        self.window.geometry('800x800')
        self.window.configure(background = "black")
         
        #center this label
        lbl1 = Label(self.window, text="Login", bg="black", fg="white", font="none 24 bold")
        lbl1.config(anchor=CENTER)
        lbl1.pack()
         
         
        lbl2 = Label (self.window, text="TeRmR", bg="black", fg="white", font="none 12 bold")
        lbl2.config(anchor=CENTER)
        lbl2.pack()


        lbl3 = Label (self.window, text="name", bg="black", fg="white", font="none 12 bold")
        #lbl3.grid(row = 1, column = 0, sticky = W, pady = 2)
        lbl3.config(anchor=CENTER)
        lbl3.pack()


        self.myEntry = Entry(self.window, width=20)
        #myEntry.grid(row = 0, column = 1, pady = 2) 
        self.myEntry.focus()
        self.myEntry.bind("<Return>",self.returnEntry)
        self.myEntry.pack()

        lbl4 = Label (self.window, text="password : ", bg="black", fg="white", font="none 12 bold")
        #lbl3.grid(row = 1, column = 0, sticky = W, pady = 2)
        lbl4.config(anchor=CENTER)
        lbl4.pack()


        self.myEn = Entry(self.window, show=' ',  width=20)
        #myEntry.grid(row = 0, column = 1, pady = 2) 
        self.myEn.focus()
        self.myEn.bind("<Return>",self.returnEntry)
        self.myEn.pack()



        # Create the Enter button
        self.enterEntry = Button(self.window, text= "login", command=self.returnEntry, height = 1)
        #enterEntry.configure(width=3)
        self.enterEntry.pack(fill=X)
         
        # Create and emplty Label to put the result in
        self.resultLabel = Label(self.window, text = "", bg="black", fg="white")
        self.resultLabel.pack(fill=X)

        self.window.mainloop()

    def returnEntry(self):
        global host
        global s
        n = self.myEntry.get()
        print(self.myEntry.get())
        p = self.myEn.get()
        if(s==1):
            port=2005
            print("sent ssh packet")
        else:
            port=2004
            print("sent telnet packet")
        soc.connect((host,port))
        msg=n+p
        soc.send(msg.encode('ascii'))
        if(soc.recv(1024).decode('ascii')):
                self.resultLabel.config(text="welcome "+n+"")
                self.window.withdraw()
                self.comments()
        else:
                self.resultLabel.config(text="enter correct password")
        self.myEn.delete(0,END)
        self.myEntry.delete(0,END)

    def comments(self):
        global soc,s
        print("Connection Established")
        while(1):
            a=input(">>>")
            print("input :",str(a))
            if a=="exit":
                print("Connection terminated")
                soc.close()
                break
            elif a=="clear":
                os.system("clear")
            else:
                com=a.split()
                if(len(com)>1):
                    com1=com[0]+" "+com[1]
                else:
                    com1=com
                if(com[0] in l or com1 in l):
                    print("Permission denied")
                else:
                    soc.send(a.encode('ascii'))
                    rep=soc.recv(1024).decode('ascii')
                    rep=rep.split("*")
                    if(s==0):
                        print("Working directory : ",rep[0])
                        for i in range(1,len(rep)):
                            print(rep[i])
                    else:
                        if(com[0]=="cd" or com==[0]=="pwd"):
                            ch=checksum(rep[0])
                            if ch==rep[1]:
                                print("Working directory : ",rep[0])
                            else:
                                print("Error in data")
                        else:
                            m1=rep[0]+rep[1]
                            ch=checksum(m1)
                            if str(ch)==rep[2]:
                                print("Working directory : ",rep[0])
                                print("\n",rep[1])
                            else:
                                print("Error in data")

class start():
    def __init__(self):
        self.window = Tk()
        self.window.geometry('800x800')
        self.window.configure(background = "black");

        #center this label
        lbl1 = Label(self.window, text="List", bg="black", fg="white", font="none 24 bold")
        lbl1.config(anchor=CENTER)
        lbl1.pack()

        lbl2 = Label (self.window, text="Enter something here:", bg="black", fg="white", font="none 12 bold")
        lbl2.config(anchor=CENTER)
        lbl2.pack()

        lbl3 = Label (self.window, text="ip packet", bg="black", fg="white", font="none 12 bold")
        #lbl3.grid(row = 1, column = 0, sticky = W, pady = 2)
        lbl3.config(anchor=CENTER)
        lbl3.pack()

        self.myEntry = Entry(self.window, width=20)
        #myEntry.grid(row = 0, column = 1, pady = 2)
        self.myEntry.focus()
        self.myEntry.bind("<Return>",self.returnEntry)
        self.myEntry.pack()

        self.lbl4 = Label (self.window, text="port : ", bg="black", fg="white", font="none 12 bold")
        #lbl3.grid(row = 1, column = 0, sticky = W, pady = 2
        self.lbl4.config(anchor=CENTER)
        self.lbl4.pack()

        self.myEn = Entry(self.window, width=20)
        #myEntry.grid(row = 0, column = 1, pady = 2)
        self.myEn.focus()
        self.myEn.bind("<Return>",self.returnEntry)
        self.myEn.pack()

        lbl5 = Label (self.window, text="Connection method (Telnet/ssh): ", bg="black", fg="white", font="none 12 bold")
        #lbl3.grid(row = 1, column = 0, sticky = W, pady = 2)
        lbl5.config(anchor=CENTER)
        lbl5.pack()

        self.myE = Entry(self.window, width=20)
        #myEntry.grid(row = 0, column = 1, pady = 2)
        self.myE.focus()
        self.myE.bind("<Return>",self.returnEntry)
        self.myE.pack()

        # Create the Enter button
        self.enterEntry = Button(self.window, text= "Enter", command=self.returnEntry, height = 1)
        #enterEntry.configure(width=3)
        self.enterEntry.pack(fill=X)

        # Create and emplty Label to put the result in
        self.resultLabel = Label(self.window, text = "", bg="black", fg="white")
        self.resultLabel.pack(fill=X)

        self.window.mainloop()

    def show(self):
        self.window.withdraw()
        s2=sta()
        s2.window.update()
        s2.window.deiconify()

    def returnEntry(self):
        global s
        ip = self.myEntry.get()
        p = self.myEn.get()
        c = self.myE.get()
        if(p=="2005" and c=="ssh"):
            self.resultLabel.config(text="IP : "+ip+" \nPORT : "+p+"\nConnection Method : "+c+" ")
            s=1
            self.show()
        elif(p=="2004" and c=="telnet"):
            self.resultLabel.config(text="IP : "+ip+" \nPORT : "+p+"\nConnection Method : "+c+" ")
            self.show()
        else:
            self.resultLabel.config(text="error....\nentered details:\nIP : "+ip+" \ngive correct port and connection method")
            self.myEn.delete(0,END)
            self.myE.delete(0,END)
                #self.myEntry.delete(0,END)
        #else:
         #   self.resultLabel.config(text="error....\nentered details:\nIP : "+ip+" \nPORT : "+p+"\nConnection Method : "+c+"\ngive correct info")
           # self.myEn.delete(0,END)
            #self.myE.delete(0,END)
            #self.myEntry.delete(0,END)



s1=start()

