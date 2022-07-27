> Ref
>- [Ubuntu的Linux内核安装与切换](https://zhaoxuhui.top/blog/2021/02/20/ubuntu-linux-kernel-installation.html)
>- [Ukuu install error](https://askubuntu.com/questions/1074350/unable-to-install-ukuu-kernel-updater)  
>- [Ubuntu Bluetooth connection suspending](https://zhongguo.eskere.club/%E5%A6%82%E4%BD%95%E4%BF%AE%E5%A4%8Dubuntu-linux%E4%B8%AD%E7%9A%84%E8%93%9D%E7%89%99%E8%BF%9E%E6%8E%A5%E9%97%AE%E9%A2%98/2021-05-12/)
>- [Ubuntu wake up after suspending](https://ifttl.com/wakeup-suspended-ubuntu-with-wireless-bluetooth-mouse/)
>- [Ubuntu bluetooth lost connection](https://blog.csdn.net/yanglei0385/article/details/81840072)
>- [Install Ubuntu on WSL2 on Windows 11 with GUI support](https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-11-with-gui-support#1-overview)
>- [Install MySQL on WSL](https://kontext.tech/article/615/install-mysql-on-wsl)
>- [How to install MySQL on WSL2](https://pen-y-fan.github.io/2021/08/08/How-to-install-MySQL-on-WSL-2-Ubuntu/)
>- [MySQL won't start - error: su...](https://stackoverflow.com/questions/62987154/mysql-wont-start-error-su-warning-cannot-change-directory-to-nonexistent)
>- [MySQL Failed! Error: SET PASSWORD...](https://exerror.com/failed-error-set-password-has-no-significance-for-user-rootlocalhost-as-the-authentication-method-used-doesnt-store-authentication-data-in-the-mysql-server/)

# 1. Create a new acount  
TBD  

# 2. The root mode
For the first time you entering the system, the root password is randomly generated. You need to setup for the root password by the following command.  
```bash
sudo passwd  # Set the password
su root  # Run root mode  
exit  # Exit root mode
```  

# 3. Change the username  
```bash
vi /etc/hostname  
vi /etc/hosts
```

# 4. Change the Keyboard Format  
```bash
sudo dpkg-reconfigure keyboard-configuration
```

# Install tools & packages  
## Network tool  
- Install 
```bash
sudo apt install net-tools
sudo apt install traceroute  # route trace
sudo apt install ssh
```
- Command  
```bash
# check network info
ifconfig 

# analyse network topology
traceroute <url>

# check public ip
curl ifconfig.me  
curl cip.cc  
curl ipinfo.io

# open ssh and check the port  
sudo service ssh start
sudo netstat -nlap|grep sshd|grep tcp|grep LISTEN
```

## Curl  
It is a command line tool for downloading or shipping data through the internet.
- Install  
```bash
sudo apt install curl
```
- Command  
```bash
curl <options> <URL>
curl ipinfo.io  # get the ip address of Wide Area Network
```
## SSH tool  
- Install  
```bash
sudo apt install ssh
```

## Device manager  
- Install  
```bash
sudo apt instal hwinfo
```
- Launch  
   1. Terminal  
   ```bash
   hwinfo --short
   ```
   2. GUI  
   Search software "hardinfo"

## Ubuntu Kernel  Upgrade Utility (ukuu)  
Ukuu is a tool to install and upgrade Linux kernel.  
- Install  
While the licence of `ukuu` is no longer freely provided, we need to download the `.deb` from github and install it.
```bash
wget https://github.com/teejee2008/ukuu/releases/download/v18.9.1/ukuu-v18.9.1-amd64.deb
sudo dpkg -i ukuu-v18.9.1-amd64.deb
``` 
- Launch  
```bash
sudo ukuu-gek  # desktop GUI
sudo ukuu  # server CLI
```

## Different between `apt` / `apt-get` / `yum`  
`yum` is for RedHat packages `rpm`.  
```bash
yum install <pkg>
yum remove <pkg>
yum update <pkg>
```

`apt-get` is for debian packages `deb`.  
```bash
apt-get install <pkg>
apt-get remove <pkg>
apt-get update <pkg>
```

`apt` is an updating version of `apt-get`  
```bash
apt install <pkg>
apt remove <pkg>
apt update <pkg>
apt list
```
# 5. Setup remote awake  
## Check the state of `wake on lan`  
```bash
# get the logical name of network interface  
ifconfig
sudo lshw -class network

# check the state of `wake on lan`
sudo ethtool <name of network interface> |grep Wake-on
# g: permitted  d: denied
```

# 6. Setup working environment    
## Anaconda 
Download the `.sh` file through by `curl <url>`, and then run the following command.  
```bash
sha256sum <.sh file name>
bash <.sh file name>
print("hello")
```

## VSCode 

## MySQL  
1. installation  
   ```bash
   sudo apt install mysql-server mysql-client  
   
   # check the version 
   mysql --version  

   # service status 
   sudo service mysql status  # check the status
   sudo service mysql start  # start mysql
   sudo service mysql stop  # stop mysql  
   sudo service mysql restart  # restart mysql

   # get into the client  
   sudo mysql -u root -p
   ```  
   If you meet the problem `su: warning: cannot change directory to /nonexistent: No such file or directory`, try the following commands.  
   ```bash
   sudo service mysql stop
   sudo usermod -d /var/lib/mysql/ mysql
   sudo service mysql start
   ```
2. query
   ```bash
   SELECT
   ```

# 7. Shortcut  
- Super  
Open the search menu.  
- Super + L  
Lock.  
- Ctrl + Alt + T  
Open the terminal.    
- Super + D  
Show the desktop.  
- Ctrl + Alt + ↑↓  
Change the workspace.  

# 8. Bash command & shortcut  
## Command  
```bash
# system
uname -srm  # show kernal name + release version + hardware framework name
dpkg --get-selections | grep linux  # show all kernals

lshw  # show hardware
lsusb  # show usb devices

cat /etc/shadow  # show all users

pwd  # show working directory
mkdir <dir name>  # make new directory
rmdir <dir name>  # remove a directory
touch <file name>  # make new file 
rm <file name>  # remove a file
cp <src> <dst>  # copy scr to dst
mv <src> <dst>  # move or rename file from src to dst

# unzip file
tar -xvzf <file name> -C <target folder>

# vi
vi <file name>  # open or create file
i  # insert

h  # left move
l  # right move
j  # down move
k  # up move

Esc  # command mode
:w  # write file
:wq  # write and quit
:q  # quit

# nano
nano <file name>  # open or create file
ctrl + x  # exit

# ssh
ssh <name>@<hostname> -p <port>
```  

## Shortcut  
1. copy & paste
   Ctrl + Shift + c/v  
2. 

# 0. P.S. Install ubuntu under win11  
Follow the instruction of [Ubuntu on WSL2 on Windows 11](https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-11-with-gui-support#1-overview)  

## command  
```bash
# 1
wsl -d <your system name>
wsl -d Ubuntu  
# 2
bash  
```
## remote connection  
1. Since the `openssh-server` cannot work properly, we need to reinstall this package.  
   ```bash
   sudo apt remove openssh-server
   sudo apt install openssh-server
   ```
2. Write `/etc/ssh/sshd_config`.
   ```bash
   sudo nano /etc/ssh/sshd_config  

   Port 2222
   PermitRootLogin yes
   PasswordAuthentication yes
   ```

