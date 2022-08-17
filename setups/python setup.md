# python setup

## 安装 anaconda  

建议安装选项不要选 "for all users"， 而是选择 "just for me"。  
Linux 在非 root 下安装，将在用户目录下自动创建 `anaconda3` 目录。

## 虚拟环境

需要安装 jupyter 才能正常使用交互式窗口。

```bash
# create env with package
conda create -n <env name> python=3.9 jupyter

# remove env
conda remove -n <env name> --all

# install package
conda install jupyter
conda install ipython
conda install --channel conda-forge geopandas
```

## PowerShell 自动启动 conda 环境  

> 参考链接:
>
>- [powershell自动激活conda环境](https://www.cxybb.com/article/qq_44275286/105001282)

```bash
$PROFILE | Format-List -Force  %查看所有配置文件路径%
```  

使用管理员模式打开 PowerShell 或者 Anaconda PowerShell Prompt，依次执行以下命令：

```bash
Set-ExecutionPolicy RemoteSigned
conda init powershell
conda config --set auto_activate_base False  %取消自动启动 conda 环境%
```  

## Install VSCode

### Shortcut

change the `when` value of `jupyter.execSelectionInteractive`.  

```text
editorTextFocus && !findInputFocussed && !jupyter.ownsSelection && !notebookEditorFocused && !replaceInputFocussed && editorLangId == 'python'

```

## 命令行中使用 conda 与 pip 命令  

### 代理问题 HTTP ERROR

> 参考链接：

- [Windows的命令行下设置网络代理](https://blog.csdn.net/sptoor/article/details/8723025)
在系统变量中添加(不是用户变量)以下两条，设置全局代理 。可解决因为挂梯子导致的 httperror 的问题

```text
HTTP_PROXY = http://127.0.0.1:7890
HTTPS_PROXY = http://127.0.0.1:7890
```  

### 常用命令

```bash
conda deactivate  
conda activate
conda list
conda create --name <my env> python=3.8
conda install <package=version>
```
