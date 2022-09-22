# git学习笔记

> 参考链接
>
>- [Github简明教程](https://www.runoob.com/w3cnote/git-guide.html)
>- [图解 Git](https://www.runoob.com/w3cnote/git-graphical.html)
>- [Github详解](https://blog.csdn.net/Hanani_Jia/article/details/77950594)
>- [Github教程](https://blog.csdn.net/rj597306518/article/details/71307757)
>- [Connecting to Github with SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
>- [A collection of useful .gitingore](https://github.com/github/gitignore)

## 1 配置

### 1.1 安装Git

- Windows  
下载[Git for windows](http://msysgit.github.io/)  
- Linux (Ubuntu)  

```bash
sudo apt install git
```

### 1.2 配置本地ssh

1. Generating a new local SSH key

    ```Bash
    ssh-keygen -t ed25519 -C your_email_address 
    ssh-keygen -t rsa -b 4096 -C your_email_address # use this instead if your system doesn't support ed25519
    ```  

2. Adding your SSH key to your account. The public key is usually stored in the folder `.ssh/`. Cpoy the content of `id_rsa.pub` to *GitHub -->> Settings -->> SSH and GPG keys -->> New SSH key*. Verify the connection by the following command.  

    ```bash
    ssh -T git@github.com
    > Hi username! You've successfully authenticated...
    ```

3. Step 2

```Bash
git config --global user.name your_name
git config --global user.email your_email_address
```

### 1.3 设置代理

走代理可以显著提升下载速度

```Bash
# 只对github.com
git config --global http.https://github.com.proxy socks5://127.0.0.1:<proxy port number>

# 取消代理
git config --global --unset http.https://github.com.proxy
```

## 2 常用命令

### 2.1 Start a repository with different situations

Before doing this, make sure you have set `user.name` and `user.email` in git setting (see 1.2 step2).

- remote empty repository & local empty folder
    1. Create a remote empty repository by pressing [new button](https://github.com/new).  
    2. Start with `git init` by creating a local folder (you'd better build a folder with the same name as the remote repository).  

        ```Bash
        mkdir name_of_the_repository && cd name_of_the_repository
        echo "# SomeRepo" >> README.md
        git init 
        git add README.md  

        # only after the first commit of a repository can you change or rename branch name
        git commit -m "first commit"
        git branch -M main  # -M: force move to branch main

        git remote add origin url_of_the_repository  # you can choose either HTTPS or SSH here
        git push -u origin main
        ```

        Or you can start with `git clone` but not `git init`.

        ```bash
        git clone url_of_the_repository
        cd name_of_the_repository

        echo "# SomeRepo" >> README.md
        git add README.md

        # only after the first commit of a repository can you change or rename branch name
        git commit -m "first commit"
        git branch -M main  # -M: force move to branch main

        git push -u origin main     
        ```

- remote non-empty repoitory & local empty folder
    1. Create a remote repository with `README.md` or `.ignore`. Or simply you can start with an existing repository.  
    2. Start with `git init` by creating a local folder(you'd better build a folder with the same name as the remote repository).  

        ```Bash
        mkdir name_of_the_repository && cd name_of_the_repository
        git init
        git remote add origin url_of_the_repository  # you can choose HTTPS/SSH here 

        # only after pulling the remote branch and commit to local can you change or rename branch name
        git pull origin main
        git branch -M main

        echo "test" >> test.txt
        git add text.txt
        git commit -m "local commit"
        git push -u origin main
        ```

        Or you can start with `git clone` but not `git init`.

        ```bash
        git clone url_of_the_repository
        cd name_of_the_repository

        echo "test" >> test.txt
        git add text.txt
        git commit -m "local commit"
        git push -u origin main        
        ```

- remote non-empty repository & local non-empty folder
    1. Create a remote repository with `README.md` or `.ignore`. Or simply you can start with an existing repository.  
    2. Start with `git init` by creating a local folder(you'd better build a folder with the same name as the remote repository).  

        ```Bash
        mkdir name_of_the_repository && cd name_of_the_repository
        git init
        git remote add origin url_of_the_repository  # you can choose HTTPS/SSH here 

        # only after pulling the remote branch and commit to local can you change or rename branch name
        git pull origin main
        git branch -M main

        echo "test" >> test.txt
        git add text.txt
        git commit -m "local commit"
        git push -u origin main
        ```

### 2.2 建立本地仓库

- 使用本地文件夹  

   ```bash
   cd <path>
   git init
   ```

- 克隆远程仓库

    ```bash
    git clone <the web URL>
    ```

### 2.3 工作流  

将改动提交到本地`HEAD`

```bash
git add <filename>  # 提交改动
git add .  # 提交所有改动

git commit -m "<tips>"
```

### 2.4 推送改动

```bash
git push origin master
```
