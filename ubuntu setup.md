> Ref
- [Ubuntu的Linux内核安装与切换](https://zhaoxuhui.top/blog/2021/02/20/ubuntu-linux-kernel-installation.html)
- [Ukuu install error](https://askubuntu.com/questions/1074350/unable-to-install-ukuu-kernel-updater)  
- [Ubuntu Bluetooth connection suspend](https://zhongguo.eskere.club/%E5%A6%82%E4%BD%95%E4%BF%AE%E5%A4%8Dubuntu-linux%E4%B8%AD%E7%9A%84%E8%93%9D%E7%89%99%E8%BF%9E%E6%8E%A5%E9%97%AE%E9%A2%98/2021-05-12/)

# Create a new acount  
TBD  

# The root mode
For the first time you entering the system, the root password is randomly generated. You need to setup for the root password by the following command.  
```bash
sudo passwd  # Set the password
su root  # Run root mode  
exit  # Exit root mode
```  

# Change the username  
```bash
vi /etc/hostname  
vi /etc/hosts
```

# Change the Keyboard Format  
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
```

## Curl  
- Install  
```bash
sudo apt install curl
```
- Command  
```bash
curl <options> <URL>
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

# Setup working environment    
- Anaconda  
- VSCode 

# Shortcut  
- Super  
Open the search menu.  
- Super + L  
Lock  
- Ctrl + Alt + T  
Open the terminal.    
- Super + D  
Show the desktop.  
- Ctrl + Alt + ↑↓  
Change the workspace  

# Bash command & shortcut  
- Command  
```bash
# system
uname -srm  # show kernal name + release version + hardware framework name
dpkg --get-selections | grep linux  # show all kernals

lshw  # show hardware
lsusb  # show usb devices

pwd  # show working directory
mkdir <dir name>  # make new directory
touch <file name>  # make new file 
cp <src> <dst>  # copy scr to dst
mv <src> <dst>  # move or rename file from src to dst


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
```  

- Shortcut  
   1. Ctrl + Shift + c/v  