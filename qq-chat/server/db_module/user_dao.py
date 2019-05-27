# order_dao.py
# 订单数据访问对象
from server.db_module.db_helper import *
from sqlalchemy import create_engine


class UserDao:
    #构造函数
    def __init__(self):
        self.db_helper = DBHelper()  #创建DBHelper对象
        self.db_helper.open_conn()   #打开数据库连接
        cursor=self.db_helper.db_conn.cursor()
        # cursor.execute("set character_set_client=utf8;")
        # cursor.execute("set character_set_connection=utf8;")
        # cursor.execute("set character_set_results=utf8;")
        # cursor.execute("set character_set_server=utf8;")
        # cursor.execute("set collation_server = utf8_general_ci;")
        # self.db_helper.db_conn.commit()
        cursor.execute("show variables like 'char%';")
        a=cursor.fetchall()
        print(a)

        cursor.close()


    #析构函数
    def __del__(self): 
        self.db_helper.close_conn()  #关闭数据库连接 

    #根据用户名查询用户信息
    def query_info_by_uname(self, uname):
        # cursor = self.db_helper.db_conn.cursor()
        # cursor.execute("show variables like 'character%';")
        # a = cursor.fetchall()
        # print(a)
        sql = "select * from users where uname = '%s'" % uname
        result = self.db_helper.do_query(sql)
        if not result:
            print("查询返回空对象")
            return None
        infos = result[0]
        if not infos:
            print("查询返回空对象")
            return None
        user_info={}
        user_info["uname"]=infos[1]
        user_info["uage"]=infos[3]
        user_info["usex"]=infos[2]
        user_info["uaddr"]=infos[5]
        return user_info

    #注册用户
    def insert_user(self,user_info):
        sql="insert into users(uname,usex,uage,utel,uaddr,upasswd,utime) VALUES ('%s','%s','%d','%s','%s','%s',now())"\
        %(user_info["uname"],user_info["usex"],int(user_info["uage"]),user_info["utel"],
          user_info["uaddr"],user_info["upasswd"])
        result = self.db_helper.do_update(sql)
        if not result:
            return False
        else:
            return True

    #查询用户登录ip地址
    def query_ip(self,uname):
        sql="select lip,lport from logins where luname='%s'"%uname
        result = self.db_helper.do_query(sql)
        return result[-1]

    #添加好友
    def insert_friend(self,uname1,uname2):
        sql="insert into friends(uname1,uname2,ftime)\
        VALUES('%s','%s',now()) "%(uname1,uname2)
        result = self.db_helper.do_update(sql)
        res = True if result else False
        return res

    #查询好友列表
    def query_friends(self,uname):
        sql1="select uname1 from friends WHERE uname2='%s'"%uname
        sql2="select uname2 from friends WHERE uname1='%s'"%uname
        result1 = self.db_helper.do_query(sql1)
        result2 = self.db_helper.do_query(sql2)
        result=list(result1)+list(result2)
        li=[]
        for item in result:
            li.append(item[0])
        return li


    #查询用户是否存在
    def query_isexist(self,uname):
        sql="select uname from users WHERE uname='%s'"%uname
        result = self.db_helper.do_query(sql)
        res=True if result else False
        return res

    #验证用户名和密码
    def check_user(self,uname,upasswd):
        sql="select uname,upasswd from users WHERE uname='%s' and upasswd='%s'"%(uname,upasswd)
        result = self.db_helper.do_query(sql)
        res = True if result else False
        return res

    #添加登录信息
    def insert_logins(self,login_info):
        sql="insert into logins(luname,lip,lport,ltime) VALUES('%s','%s','%d',now())"\
        %(login_info["lname"],login_info["lip"],login_info["lport"])

        result = self.db_helper.do_update(sql)
        res = True if result else False
        return res

    #模糊查询用户
    def query_users_by_uname(self,uname):
        sql="select uname from users WHERE uname LIKE '%s'"%uname
        result = self.db_helper.do_query(sql)
        li=[]
        for item in result:
            li.append(item[0])
            # print(li)
        return li





if __name__ == "__main__":
    user_dao=UserDao()
    user_info={"uname":"jack","uage":20,"usex":"boy","uaddr":"","utel":"","upasswd":"123"}
    # res=user_dao.insert_user(user_info)
    res=user_dao.query_info_by_uname("jack")
    uname1="wang"
    uname2="zhang"
    # res=user_dao.insert_friend(uname1,uname2)
    # res=user_dao.query_users_by_uname('jack')
    # res=user_dao.check_user("jack","123")
    print(res)
