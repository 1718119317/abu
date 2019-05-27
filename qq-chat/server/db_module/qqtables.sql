# 用户表(用户名、密码、性别、电话、邮箱、所在地，注册时间)
# 好友表(好友用户名、用户名、添加时间)
# 登录信息表(登录编号、登录IP、端口号、登录时间、是否在线、用户名)
CREATE TABLE users(
  uid INT AUTO_INCREMENT UNIQUE ,
  uname VARCHAR(32) PRIMARY KEY ,
  usex VARCHAR(16) NOT NULL ,
  uage VARCHAR(32),
  utel CHAR(11),
  uaddr VARCHAR(128),
  upasswd VARCHAR(32) NOT NULL ,
  utime DATE
)DEFAULT CHARSET='utf8';

CREATE TABLE friends(
  fid INT AUTO_INCREMENT UNIQUE,
  uname1 VARCHAR(32) NOT NULL ,
  uname2 VARCHAR(32) NOT NULL ,
  ftime DATE
)DEFAULT CHARSET='utf8';

CREATE TABLE logins(
  lid INT AUTO_INCREMENT UNIQUE,
  luname VARCHAR(32) NOT NULL ,
  lip VARCHAR(32),
  lport INT,
  ltime DATE
)DEFAULT CHARSET='utf8';

INSERT INTO users(uname,usex,uage,utel,uaddr,upasswd,utime) VALUES ("路飞","男",17,15298685848,"","123456",now());
INSERT INTO users(uname,usex,uage,utel,uaddr,upasswd,utime) VALUES ("索隆","男",19,15298685848,"","123456",sysdate());
INSERT INTO friends(uname1, uname2, ftime) VALUES ("路飞","索隆",now());
INSERT INTO logins(luname, lip, lport, ltime) VALUES ("路飞","192.168.0.108",5000,now());