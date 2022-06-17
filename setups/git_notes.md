# git学习笔记
> 参考链接
>- [Github简明教程](https://www.runoob.com/w3cnote/git-guide.html)
>- [Github详解](https://blog.csdn.net/Hanani_Jia/article/details/77950594)
>- [Github教程](https://blog.csdn.net/rj597306518/article/details/71307757)

## 配置
### 安装Git
下载[Git for windows](http://msysgit.github.io/)

### 配置本地ssh
```Bash
ssh-keygen -t rsa -C "<your email address>"
```
将生成的`id_rsa.pub`内容复制到  
GitHub->Settings->SSH and GPG keys->New SSH key  
中 然后在git Bash 里设置账号
```Bash
ssh -T git@github.com
git config --global user.name "<your name>"
git config --global user.email "<your email address>"
```

### 设置代理
走代理可以显著提升下载速度
```Bash
# 只对github.com
git config --global http.https://github.com.proxy socks5://127.0.0.1:<proxy port number>

# 取消代理
git config --global --unset http.https://github.com.proxy)
```

## 常用命令
### 建立本地仓库
- 使用本地文件夹
```
cd <path>
git init
```
- 克隆远程仓库
```
git clone <the web URL>
```

### 工作流  
将改动提交到本地`HEAD`
```
git add <filename>  # 提交改动
git add .  # 提交所有改动

git commit -m "<tips>"
```

### 推送改动
```
git push origin master
```
