> 参考链接:
- [Windows的命令行下设置网络代理](https://blog.csdn.net/sptoor/article/details/8723025)

# 解决办法  
在系统变量中添加(不是用户变量)以下两条即可。
```
HTTP_PROXY = http://127.0.0.1:7890
HTTPS_PROXY = http://127.0.0.1:7890
```
