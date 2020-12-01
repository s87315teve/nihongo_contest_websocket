import socket
import threading
import time
import os
import sys
import traceback
import argparse

class TCP_client():
    def __init__(self, host="127.0.0.1", port=6000, code="utf-8", buffer_size=1024):
        try:
            self.host=host
            self.port=port
            self.code=code
            self.buffer_size=buffer_size
            #self.timeout=timeout
            self.addr = (self.host, self.port)
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #建立TCP socket
            self.sock.connect(self.addr) #self.addr
            print("connected to server")
        except Exception as e:
            error_class = e.__class__.__name__ #取得錯誤類型
            detail = e.args[0] #取得詳細內容
            cl, exc, tb = sys.exc_info() #取得Call Stack
            lastCallStack = traceback.extract_tb(tb)[-1] #取得Call Stack的最後一筆資料
            fileName = lastCallStack[0] #取得發生的檔案名稱
            lineNum = lastCallStack[1] #取得發生的行號
            funcName = lastCallStack[2] #取得發生的函數名稱
            errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(fileName, lineNum, funcName, error_class, detail)
            print(errMsg)
            print("connection failed ")
    def send_msg(self, msg=""):
        try:
            msg=msg.encode(self.code)
            self.sock.send(msg)
        except Exception as e:
            error_class = e.__class__.__name__ #取得錯誤類型
            detail = e.args[0] #取得詳細內容
            cl, exc, tb = sys.exc_info() #取得Call Stack
            lastCallStack = traceback.extract_tb(tb)[-1] #取得Call Stack的最後一筆資料
            fileName = lastCallStack[0] #取得發生的檔案名稱
            lineNum = lastCallStack[1] #取得發生的行號
            funcName = lastCallStack[2] #取得發生的函數名稱
            errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(fileName, lineNum, funcName, error_class, detail)
            print(errMsg)
def run(opt):
    if opt.mode=="TCP_server":
        server=TCP_server(host=opt.host, port=opt.port, code=opt.code, buffer_size=opt.buffer, timeout=opt.timeout)
        server.start()
    elif opt.mode=="TCP_client":
        client=TCP_client(host=opt.host, port=opt.port, code=opt.code, buffer_size=opt.buffer)
        
        ID=""
        while ID=="":
            ID=input("輸入你的名字: ")
            if ID!="":
                client.send_msg(ID)
                sys_msg=client.sock.recv(client.buffer_size)
                sys_msg=sys_msg.decode(client.code)
                print(sys_msg)
                if sys_msg.find("註冊成功")!=-1:
                    #print(sys_msg)
                    print("請等待遊戲開始")
                else:
                    print("此名字已被註冊，請換一個名字")
                    ID=""


        if ID!="admin":
            while sys_msg!="start":
                sys_msg=client.sock.recv(client.buffer_size)
                sys_msg=sys_msg.decode(client.code)
                print(sys_msg)

            msg=""
            while True:
                question=client.sock.recv(client.buffer_size)
                question=question.decode(client.code)
                if question=="stop":
                    break
                print(question)
                msg=input("答え: ")
                if msg=="":
                    msg="pass"
                client.send_msg(msg)
                os.system('cls')
            print("時間到，請靜候結果")  
        
        if ID=="admin":
            msg=""
            while msg!="exit":
                msg=input("請輸入指令: ")
                if msg=="":
                    continue
                client.send_msg(msg)




    elif opt.mode=="UDP_server":
        server=UDP_server(host=opt.host, port=opt.port, code=opt.code, buffer_size=opt.buffer)
        server.start()
    elif opt.mode=="UDP_client":
        client=UDP_client(host=opt.host, port=opt.port, code=opt.code, buffer_size=opt.buffer)
        client.send_msg("connection success")
        msg=input("input msg: ")
        while msg!="exit":
            client.send_msg(msg)
            msg=input("input msg: ")
    else:
        print("argument illegal, please restart this program")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", "-m", type=str, default=None, help="select mode")
    parser.add_argument("--host", type=str,  default="127.0.0.1", help="set host IP")
    parser.add_argument("--port", "-p", type=int, default=6000, help="set host port")
    parser.add_argument("--code", "-c", type=str, default="utf-8", help="set how to encode/decode")
    parser.add_argument("--buffer", "-b", type=int, default=1024, help="setbuffer size")
    parser.add_argument("--timeout", "-t", type=int, default=None, help="set timeout")
    opt = parser.parse_args()
    print("your option:")
    print(opt)
    run(opt)
