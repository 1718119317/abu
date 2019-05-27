
from socket import *
from server.settings import *
from multiprocessing import Process,Manager
import json
from server.db_module.user_dao import UserDao


ADDR=(server_ip,server_port)


class ChatServer():
    def __init__(self):
        self.sockfd_tcp=socket()
        self.sockfd_tcp.setsockopt(SOL_SOCKET,SO_REUSEADDR,DEBUG)
        self.sockfd_tcp.bind(ADDR)
        self.sockfd_udp=socket(AF_INET,SOCK_DGRAM)
        self.sockfd_udp.bind(ADDR)
        self.dict_user_login=Manager().dict() #进程间共享字典(用户登录信息)
        self.user_dao=UserDao()

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
            self.user_process=Process(target=self.handle_request,args=(connfd,))
            self.user_process.start()

    #处理客户端发来的信息
    def handle_request(self,connfd):
        while True:
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
            elif msg_type=="C":
                self.do_chat(data)
            elif msg_type=="E":
                self.do_exit(data)

    def do_exit(self,data):
        print("%s客户端退出"%data[1])
        self.dict_user_login.pop(data[1])
        self.user_process.join()


    #发送信息给指定用户
    def send_msg(self,uname,msg):
        user_addr = self.user_dao.query_ip(uname)
        self.sockfd_udp.sendto(msg.encode(), user_addr)

    #转发聊天信息
    def do_chat(self,data):
        msg="C "+data[2]+" "+data[1]+" "+data[3]+" "+" ".join(data[4:])
        self.send_msg(data[2],msg)

    #转发添加好友请求结果信息
    def do_friend_request_result(self,data):
        if data[1] == "OK":
            self.user_dao.insert_friend(data[3],data[2])
            friend_list=self.user_dao.query_friends(data[3])
            msg = "FRR " + "OK " +"添加好友成功! "+" ".join(friend_list)
        else:
            msg ="FRR "+"NO "+"%s拒绝了您的添加:%s"%(data[1],data[3])
        self.send_msg(data[3], msg)


    #转发添加好友请求信息
    def do_friend_request(self,data):
        msg="FR "+" "+data[2]+" "+data[1]+" "+data[3]
        self.send_msg(data[2], msg)

    #登录
    def do_login(self,connfd,data):
        if data[1] in self.dict_user_login:
            msg="L " + "NO "+"不能重复登录!"
        else:
            res=self.user_dao.check_user(data[1],data[2])
            print(res)
            if res:
                friend_list=self.user_dao.query_friends(data[1])
                msg = "L " + "OK " + data[1]+" "+" ".join(friend_list)
                self.dict_user_login[data[1]]=connfd.getpeername()
                login_info={}
                login_info["lname"]=data[1]
                login_info["lip"]=connfd.getpeername()[0]
                login_info["lport"]=connfd.getpeername()[1]
                self.user_dao.insert_logins(login_info)
            else:
                msg = "L " + "NO "+"用户名或密码不正确!"
        connfd.send(msg.encode())


    #注册
    def do_register(self,connfd,data):
        str_uinfo="".join(data[1:])
        dict_uinfo=json.loads(str_uinfo)
        result=self.user_dao.insert_user(dict_uinfo)
        if result:
            msg = "R " + "OK " + dict_uinfo["uname"]
        else:
            msg="R " + "NO"
        connfd.send(msg.encode())


    # 显示查询用户结果
    def do_search_user(self, data):
        res = self.user_dao.query_users_by_uname(data[2])
        msg="SU "+data[1]+" "+" ".join(res)
        self.send_msg(data[1], msg)

    # 显示个人信息结果
    def show_user_info(self, data):
        dict_uinfo = self.user_dao.query_info_by_uname(data[2])
        msg="UI "+data[1]+" "+json.dumps(dict_uinfo)
        self.send_msg(data[1], msg)



if __name__ == '__main__':
    qq_server=ChatServer()
    qq_server.start()








