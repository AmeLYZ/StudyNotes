# git notes

> 参考链接
>
>- [Github简明教程](https://www.runoob.com/w3cnote/git-guide.html)
>- [图解 Git](https://www.runoob.com/w3cnote/git-graphical.html)
>- [Github详解](https://blog.csdn.net/Hanani_Jia/article/details/77950594)
>- [Github教程](https://blog.csdn.net/rj597306518/article/details/71307757)
>- [Connecting to Github with SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
>- [A collection of useful .gitingore](https://github.com/github/gitignore)

## 1 Setting up environment

### 1.1 Installation

- Windows  
    Download and install from [Git for Windows Setup](https://git-scm.com/download/win).  
- Linux (Ubuntu)  

    ```bash
    sudo apt install git
    ```

### 1.2 SSH conection to your account (Github)

1. Generating a new local SSH key

    ```Bash
    ssh-keygen -t ed25519 -C <your email address> 
    ssh-keygen -t rsa -b 4096 -C <your email address> # use this instead if your system doesn't support ed25519
    ```  

2. Adding your SSH key to your account. The public key is usually stored in the folder `.ssh/`. Cpoy the content of `id_rsa.pub` to *GitHub -->> Settings -->> SSH and GPG keys -->> New SSH key*. Verify the connection by the following command.  

    ```bash
    ssh -T git@github.com
    > Hi username! You've successfully authenticated...
    ```

3. Set global user information

    ```Bash
    # The name and email address here don't have to be the same with github username, it's just for identification
    git config --global user.name <your name>  
    git config --global user.email <your email address>
    ```

### 1.3 Set agent

走代理可以显著提升下载速度

```Bash
# 只对github.com
git config --global http.https://github.com.proxy socks5://127.0.0.1:<proxy port number>

# 取消代理
git config --global --unset http.https://github.com.proxy
```

## 2 Workflow

### 2.1 Start a repository

Before doing this, make sure you have set `user.name` and `user.email` in git setting (see 1.2 step2).

- remote empty repository & local empty folder
    1. Create a remote empty repository by pressing [new button](https://github.com/new).  
    2. Start with `git init` by creating a local folder (you'd better build a folder with the same name as the remote repository).  

        ```Bash
        mkdir <repository name> && cd <repository name>
        echo "# SomeRepo" >> README.md
        git init 
        git add README.md  

        # only after the first commit of a repository can you change or rename branch name
        git commit -m "first commit"
        git branch -M main  # -M: force move to branch main

        git remote add origin <repository url>  # you can choose either HTTPS or SSH here
        git push -u origin main
        ```

        Or you can start with `git clone` but not `git init`.

        ```bash
        git clone <repository url>
        cd <repository name>

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
        mkdir <repository name> && cd <repository name>
        git init
        git remote add origin <repository url>  # you can choose either HTTPS/SSH here 

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
        git clone <repository url>
        cd <repository name>

        echo "test" >> test.txt
        git add text.txt
        git commit -m "local commit"
        git push -u origin main        
        ```

- remote non-empty repository & local non-empty folder
    1. Create a remote repository with `README.md` or `.ignore`. Or simply you can start with an existing repository.  
    2. Start with `git init` by creating a local folder(you'd better build a folder with the same name as the remote repository).  

        ```Bash
        mkdir <repository name> && cd <repository name>
        git init
        git remote add origin <repository url>  # you can choose either HTTPS/SSH here 

        # only after pulling the remote branch and commit to local can you change or rename branch name
        git pull origin main
        git branch -M main

        echo "test" >> test.txt
        git add text.txt
        git commit -m "local commit"
        git push -u origin main
        ```

### 2.2 Creating a new branch

1. Check your current branch with command `git branch`.  
2. Copy current branch to a new branch and check out the new branch.  

    ```Bash
    # method 1
    git chechuot -b <new-branch> # -b means create new branch

    # method 2
    git switch -c <new-branch>
    git switch --create <new-branch>

    # method 3
    git branch <new-branch>
    git switch <new-branch>
    ```

### 2.3 Basic snapshotting

1. When some files are changed, use `git add` command.

    ```Bash
    git add <changed files>
    git add .  # add all changed files to index
    ```

2. Record all changes in the index to the repository.

    ```Bash
    git commit <commit message>
    ```

3. Push local repository to remote

    ```Bash
    git push origin <branch name>
    ```

### 2.4 Make a pull request

1. Make `New pull request` on Github.
2. The host of that repository accept the new pull request then `Squash and merge`.
3. After the new branch is merged to main branch, first delete the new branch on Github. Then delete the new branch locally.

    ```Bash
    git checkout main
    git branch -D <branch name>
    git pull origin main  # pull the new commit to local main
    ```

### 2.5 Conflicts

1. Make sure local main branch is up to date.

    ```Bash
    git checkout main  # switch branch to main
    git pull origin main 
    ```

2. Reapply new commits on main branch to new branch

    ```Bash
    git checkout <branch name>
    git rebase main
    git push -f origin <branch name>  # force push local repo to remote
    ```

### 2.3 旧内容

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

## 3 Useful commands

```Bash

git diff  # show changes between commits, commit and working tree
# run :q to exit

git add <file name>  # add file content to the index
git branch  # show current branch

git pull origin main  # pull remote repository to local
git push origin main  # push local repository to remote
```
