from socket import *
from server.settings import *
from multiprocessing import Process
import json


ADDR=(server_ip,server_port)


class ChatServer():
    def __init__(self):
        self.sockfd_tcp=socket()
        self.sockfd_tcp.setsockopt(SOL_SOCKET,SO_REUSEADDR,DEBUG)
        self.sockfd_tcp.bind(ADDR)
        self.sockfd_udp=socket(AF_INET,SOCK_DGRAM)
        self.sockfd_udp.bind(ADDR)
        self.dict_user_login={}

    def start(self):
        self.sockfd_tcp.listen(5)
        #　等待客户端连接
        while True:
            print("Waiting for connect ....")
            try:
                connfd,addr = self.sockfd_tcp.accept()
            except KeyboardInterrupt:
                print("Server exit")
                break
            print("Connect from",addr) #　客户端地址
            user_process=Process(target=self.handle_request,args=(connfd,))
            user_process.start()

    def handle_request(self,connfd):
        # 消息收发
        while True:
            # print("等待接收:...")
            data = connfd.recv(1024)
            if not data:
                break
            print("Receive message:",data.decode())
            data=data.decode().split(" ")
            msg_type=data[0]
            if msg_type=="L":
                self.do_login(connfd,data)
            elif msg_type=="R":
                self.do_register(connfd,data)
            elif msg_type == "UI":
                self.show_user_info(data)
            elif msg_type=="FR":
                self.do_friend_request(data)
            elif msg_type=="FRR":
                self.do_friend_request_result(data)
            elif msg_type == "SU":
                self.do_search_user(data)

    def do_friend_request_result(self,data):
        if data[1] == "OK":
            friend_list=["zs","lisi","赵敏","周芷若"]
            msg = "FRR " + "OK " +"添加好友成功! "+" ".join(friend_list)
        else:
            msg ="FRR "+"NO "+"%s拒绝了您的添加:%s"%(data[1],data[3])
        user_addr = self.dict_user_login[data[3]]
        self.sockfd_udp.sendto(msg.encode(), user_addr)

    def do_friend_request(self,data):
        msg="FR "+" "+data[2]+" "+data[1]+" "+data[3]
        user_addr = self.dict_user_login[data[2]]
        self.sockfd_udp.sendto(msg.encode(), user_addr)

    def do_login(self,connfd,data):
        print("L")
        friend_list = ["zs", "lisi", "赵敏", "周芷若"]
        msg = "L " + "OK " + data[1]+" "+" ".join(friend_list)
        self.dict_user_login[data[1]]=connfd.getpeername()
        connfd.send(msg.encode())
        # connfd.close()


    def do_register(self,connfd,data):
        msg = "R " + "OK " + "zs"
        connfd.send(msg.encode())
        # connfd.close()

    # 显示查询用户结果
    def do_search_user(self, data):
        # print(self.dict_user_login[0])
        res = ["lis","wang","zs"]
        msg="SU "+data[1]+" "+" ".join(res)
        user_addr = self.dict_user_login[data[1]]
        print(user_addr)
        self.sockfd_udp.sendto(msg.encode(), user_addr)

    # 显示个人信息结果
    def show_user_info(self, data):
        dict_uinfo ={"uname":"zs","uage":20,"usex":"男","uaddr":"深圳"}
        msg="UI "+data[1]+" "+json.dumps(dict_uinfo)
        #从用户登录信息字典中找到用户的IP地址
        user_addr=self.dict_user_login[data[1]]
        self.sockfd_udp.sendto(msg.encode(),user_addr)



if __name__ == '__main__':
    qq_server=ChatServer()
    qq_server.start()








