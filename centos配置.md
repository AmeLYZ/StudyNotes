# CentOS配置笔记
> 参考链接:
>- 简书 [CentOS+Flask+Nginx+uWSGI配置](https://www.jianshu.com/p/f1acbd401bed)
>- CSDN [CentOS+Flask+uWSGI+Nginx+supervisor部署](https://blog.csdn.net/yanghuan313/article/details/69214889)
>- CSDN [Flask阿里云上部署](https://blog.csdn.net/andor_zz/article/details/51622358)
>- CSDN [从0部署Flask项目](https://blog.csdn.net/zhyh1435589631/article/details/51946439)
>- [如何部署Flask项目](https://segmentfault.com/q/1010000004169782)
>- [基于Nginx+uWSGI部署Django](https://blog.igevin.info/posts/deploy-django-with-ubuntu-and-uwsgi/)
>- [nginx配置](https://www.cnblogs.com/Erick-L/p/7066455.html)
>- [nginx配置2](https://www.oschina.net/translate/serving-flask-with-nginx-on-ubuntu)
>- [uWSGI与Nginx讲解](https://blog.csdn.net/shu_8708/article/details/79068581)

## 文件传输
- 查看开放的端口
```Bash
netstat -ntlp
```
- 生成SSH密钥文件
  - 腾讯云直接生成SSH密钥文件
  - 其他终端可通过[PuTTY Gen](https://v.youhuima.cc/vultr-vps%E6%80%8E%E6%A0%B7%E8%AE%BE%E7%BD%AEssh-keys%E5%B9%B6%E7%94%A8%E4%B9%8B%E6%97%A0%E5%AF%86%E7%A0%81ssh%E7%99%BB%E5%BD%95.html)生成SSH公钥/私钥对
- 设置安全组开放22端口
- FileZilla *编辑-设置-SFTP* 中加载SSH 连接服务器


## 基础配置
### 安装依赖
```Bash
yum install 'Development tools'
```

### killall
```bash
yum install psmisc
```

### yum-config-manager
```Bash
yum install yum-utils
```

### 防火墙 firwall--cmd
- 安装
```Bash
yum install firewalld
```
- 命令
```Bash
firewall-cmd --zone=public --add-port=8080-8081/tcp --permanent //永久开启某个端口
firewall-cmd --zone=public --add-port=8080-8081/tcp //临时开启某个端口
firewall-cmd --reload  //加载设置
firewall-cmd --zone=public --list-ports --permanent //端口空格隔开 例如 8080-8081/tcp 8388/tcp 80/tcp
firewall-cmd --query-port=443/tcp  //检查端口占用情况
systemctl start firewalld.service  //开启服务
systemctl stop firewalld.service  //关闭防火墙
systemctl enable firewalld.service  //开机自动启动
systemctl disable firewalld.service  //关闭开机制动启动
```

## python配置
### 安装pip
```
yum install epel-release
yum list|grep pip
yum install python2-pip.noarch
```
### virtualenv创建虚拟环境
```
pip install virtualenv
mkdir pyenv  #创建虚拟环境文件夹
cd pyenv
virtualenv venv  #创建名为venv的虚拟环境
virtualenv venv --no-setuptools  #setuptools报错的话需这样安装
source venv/bin/activate  #激活虚拟环境
deactivate  #关闭虚拟环境
```

### conda创建虚拟环境
windows上有多个python版本时，virtualenv可能因为多个pip冲突报错，用conda来创建虚拟环境
```
mkdir pyenv  #创建虚拟环境文件夹
cd pyenv
conda create -n venv python=2.7
activate venv
deactivate
```

### 在虚拟环境中安装uWSGI
- 解决dev依赖问题
```
yum list|grep python-devel
yum install python-devel.x86_64
```
- 虚拟环境中安装uwsgi
```
pip install uwsgi
```
- 检测是否安装成功  
在虚拟环境目录下创建`test.py`
```python
def application(env, start_response):
      start_response('200 ok', [('Content-Type', 'text/html')])
      return [b'hello from uwsgi']
```
使用命令`uwsgi --http:9000 --wsgi-file test.py`,如果启动成功,访问 *[服务器公网ip]:9090* 能收到返回的字符串
- 配置文件  
在工程路径下创建`config.ini`
```ini
[uwsgi]
socket = 127.0.0.1:5000  #uwsgi 启动时所使用的地址与端口
chdir = /root/flask_restful  #指向网站目录
wsgi-file = manage.py  #python启动程序
callable = app  #python程序内用以启动application的变量名
process = 4  #处理器数
threads = 2  #线程数
buffer-size = 32768
stats = 127.0.0.1:9191  #状态检测地址
```
- 相关命令(均在虚拟环境下)
```bash
uwsgi --http :9090 --ini config.ini  #启动 http方式 指定ini文件
killall -9 uwsgi  #关闭
ps -ef|grep uwsgi  #查看进程
```


## 安装JDK
- 检测原有JDK
```
rpm -qa|grep jdk
sudo rpm -e --nodeps [jdk]
```
- 安装新的JDK
```
yum search java|grep jdk
yum install [java-version]
vi /etc/profile  #配置环境变量
source /etc/profile  #使改变生效
java -version  #检查是否安装成功
echo $JAVA_HOME  #查找JDK安装路径
```
  - 配置环境变量
```
JAVA_HOME=/usr/lib/jvm/[java-version.x86_64]
JRE_HOME=$JAVA_HOME/jre
CLASS_PATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JRE_HOME/lib
PATH=$PATH:$JAVA_HOME/bin:$JRE_HOME/bin
export JAVA_HOME JRE_HOME CLASS_PATH PATH
```
  - 检查是否安装成功  
```
[root@user]# java -version
java version "1.8.0_131"
Java(TM) SE Runtime Environment (build 1.8.0_131-b11)
Java HotSpot(TM) Client VM (build 25.131-b11, mixed mode)
```

## 安装Nginx
- 安装Nginx
```
yum install nginx
rpm -ql nginx  #查看安装路径
```
- 修改配置文件  
修改`nginx.conf`文件
```
:39  #修改端口号
:41  #修改服务器公网ip
:48
      include        uwsgi_params;
      uwsgi_pass     127.0.0.1:8001;  # 服务端口 与uwsgi配置里一致
      uwsgi_param UWSGI_PYHOME /var/www/myproject/myenv;  # 指向虚拟环境目录
      uwsgi_param UWSGI_CHDIR /var/www/myproject;  # 指向项目根目录
      uwsgi_param UWSGI_SCRIPT run:app;  # 指向启动程序
```
- 相关命令
```
service nginx start
service nginx stop
service nginx restart
service nginx reload
```

## 安装apache
- 安装
```
yum list|grep httpd  #查看是否可用
yum install httpd
vi /etc/httpd/conf/httpd.conf  #配置文件
```
  - 修改配置文件  
`httpd.conf`文件
```
：41  #监听端口
Listen 127.0.0.1:80
:95  #修改域名信息
ServerName 127.0.0.1:80
:86  #修改管理员邮箱地址
ServerAdmin root@localhost
:151  #None变成All
AllowOverride All
:164  #添加只能使用目录名称访问的文件名
DirectoryIndex index.html index.php
```
添加以下内容到文件尾
```
//server's response header（安全性）
ServerTokens Prod  
//keepalive is ON
KeepAlive On
```
- 相关命令
```
httpd
http -a stop
systemctl start httpd.service
killall httpd
chkconfig httpd on  #设置开机自动启动
```

## 安装mysql
- 安装  
https://dev.mysql.com/downloads/repo/yum/ 查询yum地址 以及官方安装指导
```
wget 'https://dev.mysql.com/get/mysql80-community-release-el7-1.noarch.rpm'  #田间rpm源
sudo rpm -Uvh platform-and-version-specific-package-name.rpm  #替换下载的rpm源
yum repolist all|grep mysql  #查看是否下载成功
sudo yum-config-manager --disable mysql80-community
sudo yum-config-manager --enable mysql55-community
yum repolist all|grep mysql  #确认是否修改成功
yum install mysql-community-server
```
- 配置文件  
文件`/etc/my.cnf`
```
[client]
default-character-set = utf8
[mysqld]
default-storage-engine = INNODB
character-set-server = utf8
collation-server = utf8_general_ci  #不区分大小写
collation-server = utf8_bin  #区分大小写
collation-server = utf8_unicode_ci  比 utf8_general_ci 更准确
```
- 相关命令
  - 启动服务
```
sudo systemctl start mysqld
sudo systemctl stop mysqld
sudo systemctl restart mysqld
sudo systemctl status mysqld  #检查运行状态
```
  - 查看默认密码 以默认密码登陆
mysql5.5默认密码为空 5.7之后默认密码用`grep`获取
``` Bash
grep 'temporary password' /var/log/mysqld.log  #mysql5.7
mysql -uroot -p
```

  - 修改密码
    - mysql5.5
``` sql
use database mysql;
update user set password=password("new password") where user="root";
flush privileges;
```
    - mysql5.7
``` sql
ALTER USER 'root'@'localhost' IDENTIFIED BY 'new password';
```
  - 创建数据库
``` sql
CREATE DATABASE <databasename> CHARACTER SET utf8;
```
- 增加对python的支持
```
yum install mysql-devel  #解决依赖
```
  - python2
```
pip install mysql-python
```
  - python3
```
pip install pymysql
```
  - 检查是否安装成功
```python
import MySQLdb  # python2
import PyMySQL  # python3
```
  - flask连接测试
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy  
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:1234@localhost:3306/test'
db = SQLAlchemy(app)
db.create_all()
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)
db.create_all()
```

## 安装Supervisor
进程守护用
https://blog.csdn.net/yanghuan313/article/details/69214889

## 常用命令
> - 系统
```
uname -a  #查看版本
ls -a  #查看当前目录文件列表
df -h  #查看系统目录情况
yum install [package] #使用CentOS知识库安装库
wget [url]  #使用网页链接安装库
scp [本地文件路径] [root@45.40.198.68:~]  #传本地文件到目录home下
lsof -i:80  #查看占用80端口的程序
kill -9 pid[进程号]  #关掉该进程
mkdir [folder]  #创建文件夹
ctrl+c  #shell中断
```
- vi
```
esc  #进入命令模式
o  #光标下插入一行
i  #光标前插入
a  #光标后插入
:wq  #保存文件并退出
:q  #不保存文件并退出
```
- yum
```
-y  #安装时自动回答yes
list  #查找可安装的所有包名
search  #搜索制定关键字的包名
install  #安装
update  #更新(避免使用yum -y update)
remove  #卸载
```
- rpm  
&emsp;rpm默认安装路径是`/usr/rpm`
```
-i  #安装
-v  #显示详细情况
-h  #显示进度
--nodeps  #不检测依赖性 不能使用这个指令
-e  #卸载
-q  #查询包
-qa  #查询全部包
-qa|grep  #查询包含关键字的包
```
