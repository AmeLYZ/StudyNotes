# python setup

## 安装 anaconda  

建议安装选项不要选 "for all users"， 而是选择 "just for me"。  
Linux 在非 root 下安装，将在用户目录下自动创建 `anaconda3` 目录。

## env & channel

The interactive window for a new environment can only launched after installation of `jupyter` and `ipython`.  
The configuration file `.condarc` is in the root directory of every environment.  

```bash
# create env with package
conda create -n <myenv> python=3.9 jupyter

# remove env
conda remove -n <myenv> --all

# install packages
conda install jupyter ipython  # multiple packages can be installed at one time
```

Different channels (source of packages) can be chosen or set when installing a package.  

```bash
# install packages from conda-forge other than default
conda install -c conda-forge geopandas
conda install --channel conda-forge geopandas 
# install packages from conda-forge, but dependencies may be installed from default
conda install conda-forge::geopandas
```

The channel can be changed permanently using `conda config`. Once this command is used, the `.condarc` file will be created.

```bash

# with parameter --env, the configuration becomes locally in current environment.
conda config --env --add channels conda-forge  # add conda-forge to the top of channel list
conda config --env --append channels conda-forge  # add conda-forge to the bottom of the list
conda config --env --remove channels conda-forge
```

Also different dependency rules can be set, the default setting is `flexible`.  

```bash
conda config --describe channel_priority
conda config --env --set channel_priority <strict/flexible/disabled>
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
conda activate <myenv>
conda list
conda create --name <myenv> python=3.8
conda install <package=version>
conda info --env
```
