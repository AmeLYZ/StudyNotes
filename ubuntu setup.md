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

# Install tools & packages  
## Network tool  
- Install 
```
sudo apt install net-tools
sudo apt install traceroute  # route trace
sudo apt install ssh
```
- Command  
```
# check network info
ifconfig 

# analyse network topology
traceroute <url>

# check public ip
curl ifconfig.me  
curl cip.cc  
```

## SSH tool  
- Install  
```
sudo apt install ssh
```

## Different between `apt` / `apt-get` / `yum`  
`yum` is for RedHat packages "rpm".  
```bash
yum install <pkg>
yum remove <pkg>
yum update <pkg>
```

`apt-get` is for debian packages "deb".  
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
- Ctrl + Shift + c/v  