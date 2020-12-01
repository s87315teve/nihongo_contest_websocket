#coding=utf-8
#websocket example
import socket
import threading
import time
import os
import sys
import traceback
import argparse
import readSupport
import random

class Game():
    def __init__(self, time=180, mode=None):
        self.player_dict={}
        self.time=time
        self.tango_list=[]
        self.mode=mode

        #讀檔
        file = open( 'tango_list.txt', 'r',encoding='utf-16')
        line = file.readline()
        while line:
            self.tango_list.append(readSupport.Tango(line.split()[0],line.split()[1]))
            line = file.readline()
        #關檔    
        random.shuffle(self.tango_list)
        for i in range(0,10):
            print(self.tango_list[i].kanji, self.tango_list[i].yomikata)

    def set_time(self, t):
        self.time=t

    def add_player(self, ID):
        self.player_list.append(ID)

    def del_player(self, ID):
        self.player_list.remove(ID)

    def print_player(self):
        print("目前已加入的玩家:{}".format(self.player_list))

    def shuffle_player_list(self):
        #shuffle
        pass
    def start(self):
        pass

class Player():
    def __init__(self):
        self.ID=""
        self.point=0
def command_process(command):
    global game
    global global_client_list
    global start_time
    try:
        print(command)
        if command=="check status":
            print("now player:")
            for ID in game.player_dict:
                print(ID)

            print("time limit {}".format(game.time))


        elif command=="print player":
            print("now player:")
            for ID in game.player_dict:
                print(ID)
        elif command.find("set time")!=-1:
            command_split=command.split()
            game.set_time(int(command_split[2]))
        elif command=="game start":
            for client in global_client_list:
                if client.player_ID!="admin":
                    client.send_msg("遊戲準備開始")
            time.sleep(1)
            for client in global_client_list:
                if client.player_ID!="admin":
                    client.send_msg("時間限制為 {} 秒".format(game.time))
            time.sleep(1)
            for i in range(5, 0, -1):
                for client in global_client_list:
                    if client.player_ID!="admin":
                        client.send_msg("距離遊戲開始還有 {} 秒".format(i))
                time.sleep(1)
                        
            for client in global_client_list:
                if client.player_ID!="admin":
                    client.send_msg("start".format(game.time))
            for client in global_client_list:
                if client.player_ID!="admin":
                    client.start()
            start_time=time.time()


                    



        else:
            print("無效的指令")
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
    
    pass


game=Game()
start_flag=False
global_client_list=[]
start_time=0
class multi_sock(threading.Thread):
    def __init__(self, conn, addr, code, buffer_size, timeout, player_ID):
        threading.Thread.__init__(self)
        self.conn=conn
        self.addr=addr
        self.code=code
        self.buffer_size=buffer_size
        self.timeout=timeout
        self.player_ID=player_ID
        print("{} connected to server".format(addr))
        
                    
    def run(self):
        global game
        global start_flag
        global start_time
        if self.timeout!=None:
            self.conn.settimeout(self.timeout)

        while self.player_ID=="admin":
            msg=self.conn.recv(self.buffer_size)
            msg=msg.decode(self.code)
            command_process(msg)
            continue
        if self.player_ID=="admin":
            return

        sys_log=""
        for count in range(0, len(game.tango_list)):
            try:
                monndai=game.tango_list[count].kanji
                self.send_msg("{}第{}問: {}".format(sys_log, count+1, monndai))


                msg=self.conn.recv(self.buffer_size)
                if not msg:
                    print("client {} {}is gone ".format(self.addr, self.player_ID))
                    print("connection closed")
                    self.conn.close()
                    break
                msg=msg.decode(self.code)
                if time.time()-start_time <= game.time:
                    #--------------------------------
                    #放function
                    point=0
                    correct=False
                    for tango in game.tango_list:
                        if monndai == tango.kanji and msg==tango.yomikata:
                            point=len(tango.yomikata)
                            correct=True
                            print("{} 答對 {} {}".format(self.player_ID, monndai, msg))
                            sys_log="恭喜你答對了\n現在你的分數是 {} 分\n\n".format(game.player_dict[self.player_ID]+point)
                            break
                    if correct==False:
                        
                        for i in range(0, min( len(game.tango_list[count].yomikata), len(msg) )):
                            if game.tango_list[count].yomikata[i]==msg[i]:
                                point+=1
                        sys_log="可惜，正確答案是: {}\n現在你的分數是 {} 分\n\n".format(game.tango_list[count].yomikata, game.player_dict[self.player_ID]+point)
                        print("{} 答錯 {} {}".format(self.player_ID, monndai, msg))

                    game.player_dict[self.player_ID]+=point

                    #--------------------------------
                    #print("recv msg: ",msg)
                else:
                    break

            except socket.timeout:
                print("{} socket timeout".format(self.addr))
                print("connection closed")
                self.conn.close()
                break
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
                self.conn.close()
                print("{} connection closed".format(self.addr))
                break
        self.send_msg("stop")

        print("玩家: {}, 分數: {}".format(self.player_ID, game.player_dict[self.player_ID]))

    def send_msg(self, msg=""):
        try:
            msg=msg.encode(self.code)
            self.conn.send(msg)
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

class TCP_server():
    def __init__(self, host="127.0.0.1", port=6000, code="utf-8", buffer_size=1024, timeout=None):
        try:
            self.host=host
            self.port=port
            self.code=code
            self.buffer_size=buffer_size
            self.timeout=timeout
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #建立socket
            self.client_list=[]
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

    def start(self):
        global game
        global global_client_list
        try:
            self.sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #讓socket可以reuse
            bind_addr=(self.host, self.port)
            self.sock.bind(bind_addr) #self.addr
            self.sock.listen()
            print("server start")
            print("server is listening to {}".format(bind_addr))
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
            print("server failed to start")
        try:
            while True:
                conn, addr = self.sock.accept()
                while True:
                    ID=conn.recv(self.buffer_size)
                    ID=ID.decode(self.code) 
                    if ID not in game.player_dict:
                        if ID !="admin":
                            game.player_dict[ID]=0                
                        self.client_list.append(multi_sock(conn=conn, addr=addr, code=self.code, buffer_size=self.buffer_size, timeout=self.timeout, player_ID=ID))
                        #self.client_list[-1].start()
                        if ID=="admin":
                            self.client_list[-1].start()

                        global_client_list=self.client_list
                        sys_log="{} 註冊成功".format(ID)
                        print(sys_log)
                        conn.send(sys_log.encode(self.code))
                        break
                    else:
                        sys_log="{} 有人取過了".format(ID)
                        print(sys_log)
                        conn.send(sys_log.encode(self.code))
                        continue
                    
        except Exception as e:
            print(e)
            pass
            
    
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
    


