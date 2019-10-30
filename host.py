#This is the centralised system that provides virtual terminal for other devices.
#Each client is handled as a thread.
#For each client, a directory is created that acts as their root directory.
#Output of each command is stored in a file which is sent over a packet.
#Commands that try to check performance of cpu,access rights and a few network based commands are denied execution
#Created by Ganga B and Subasree N


import socket
import os
import subprocess
from threading import Thread

soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp_ip=socket.gethostname()
port=2004


class ClientThread(Thread):

    def __init__(self,ip,port):
        Thread.__init__(self)
        self.ip=ip
        self.port=port

    def run(self):
        while(1):
            log=conn.recv(1024).decode('ascii')
            if(os.path.exists(log[0:4]) and log[4:]=='pass'):
                conn.send("True".encode('ascii'))
                path=os.path.abspath(log[0:4])
                os.chdir(path)
                break
            else:
                conn.send("False".encode('ascii'))


        while(1):
            tn=conn.recv(1024).decode('ascii')
            if(tn == 'pwd'):
                path=os.getcwd()
                start=path.find('log[0:4]')
                fpath=path[start:]
                print(fpath)
                conn.send(fpath.encode('ascii'))
            elif(tn == 'cd ..'):
                path=os.getcwd()
                start=path.find(log[0:4])
                fpath=path[start:]
                if(fpath == log[0:4]):
                    conn.send(fpath.encode('ascii'))
                else:
                    os.chdir('..')
                    path=os.getcwd()
                    start=path.find(log[0:4])
                    fpath=path[start:]
                    conn.send(fpath.encode('ascii'))
            elif( tn == "cd /"):
                path=os.path.abspath(log[0:4])
                os.chdir(path)
                path=os.getcwd()
                start=path.find(log[0:4])
                fpath=path[start:]
                conn.send(fpath.encode('ascii'))
            elif(tn[0:2] == 'cd'):
                path=os.path.abspath(tn[2:])
                os.chdir(path)
                path=os.getcwd()
                start=path.find(log[0:4])
                fpath=path[start:]
                conn.send(fpath.encode('ascii'))
            elif(tn == 'exit'):
                break

            else:
                out=subprocess.Popen(tn,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                op,err=out.communicate()
                op=op.decode('ascii')
                err=err.decode('ascii')
                path=os.getcwd()
                start=path.find(log[0:4])
                fpath=path[start:]
                conn.send((fpath+'*'+op+'*'+err).encode('ascii'))


if __name__ == '__main__':
    print("-------------------------------------------------------------TeRmR Server-------------------------------------------------------------")
    soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("\n\nSocket successfully created\n\n")
    soc.bind((tcp_ip,port))
    clients=[]

    while True:
        soc.listen(5)
        print("\nWaiting for TCP Clients------------------------------------------------------")
        (conn,(ip,port))=soc.accept()
        client=ClientThread(ip,port)
        print("\nNew Thread from ip:"+ip+"\nport:",port)
        client.start()
        clients.append(client)
    
    for c in clients:
        c.join()

