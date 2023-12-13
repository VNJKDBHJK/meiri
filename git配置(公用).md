# git配置（公用）

[TOC]



快速跳转：

<a href="#拉取项目">拉取项目</a>

<a href="#上传-新建仓库">上传-新建仓库</a>

<a href="#已有仓库继续上传">已有仓库继续上传</a>

## 魔法

哦好吧，你们可能已经有魔法了，这里只给出推荐

[v2rayA官方文档](https://v2raya.org/docs/prologue/introduction/)

[奇妙的代理](https://xn--mesr8b36x.net/#/dashboard)

## 1. 简单了解github

什么是 Git？ Git 是一个版本控制系统，它可以跟踪代码的更改，并允许 多人协作开发一个项目。Git 能够记录代码的历史版本，从 而可以轻松地回滚到以前的版本，或者在多个分支上同时 开发不同的功能。 

什么是 GitHub？ GitHub 是一个基于 Git 的代码托管平台，它让开发者可以 在云端存储代码，并与其他人共享和协作开发项目。

<img src="https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312131934806.png" alt="image-20231213193434607" style="zoom: 67%;" />

> 这是github的初始页面

 $\textcolor{green}{这里是你的一部分常用项目}$

 $\textcolor{red}{这里是你follow的git主}$

 $\textcolor{orange}{点进去试试}$

<img src="https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312132117340.png" alt="image-20231213211733126" style="zoom:67%;" />

> 这是点进去后的侧边栏，里面是你的一些配置，点击 $\textcolor{orange}{这里}$进入你的主页

<img src="https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312132121244.png" alt="image-20231213212111943" style="zoom:67%;" />

 $\textcolor{orange}{这里可以查看你的followers(跟随者)following(跟随的人)}$点进去看看没准就能发现学姐的主页捏

 $\textcolor{green}{这里是自述}$，github推出了可以展示自己基础信息的模块

<img src="https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312132124583.png" alt="image-20231213212427467" style="zoom:67%;" />

在以你名字命名的存储库中新建README.md文件（当然也可以是别的），进入编辑在代码中可以放一些你想放的东西上去，[关于自述文件](https://docs.github.com/zh/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)

 $\textcolor{red}{这里是你的存储库入口}$

好的，到此你已经简单了解了github，其他功能请自行探索

## 2. 关于如何将项目拉到本地

> 如果你遇到紧急需要完成的大作业，但你根本不会做，这时你应该_____________
>
> ~~(拉取别人的项目)~~ 努力完成项目，是的，好好学习，天天向上

当你特别喜欢我的某一篇笔记，你可以直接下载

<img src="https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312132137804.png" alt="image-20231213213757692" style="zoom:67%;" />

但如果你想要的有

![image-20231213214538663](https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312132145699.png)

这么多，这时应该将整个项目拉取到本地

### 安装git

首先[下载git](https://www.git-scm.com/download/)

以下是 Windows 系统的操作流程

<img src="https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312132150614.png" alt="image-20231213215031502" style="zoom: 80%;" />

<img src="https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312132150658.png" alt="image-20231213215054582" style="zoom:80%;" />

[奇妙的传送门](https://registry.npmmirror.com/binary.html?path=git-for-windows/)

点击next至

<img src="https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312132152689.png" alt="image-20231213215254626" style="zoom:80%;" />

这里，不建议配置到C盘，更改自己的路径

选择组件

此处默认即可，但我选择了一个新功能。

![img](https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312132154337.webp)

选择Git默认的编辑器

**此处选择默认即可，有特殊爱好亦可更换。**

![img](https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312132154341.webp)

选择执行git init命令时创建的分支名

第一个选项是使用 `master` 作为分支名，第二个选项自定义分支名。此处默认即可。

![img](https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312132154354.webp)

设置环境变量PATH

配置一是 “仅从 Git Bash 使用 Git” 。这是最安全的选择，因为您的 PATH 根本不会被修改。您只能使用 Git Bash 的 Git 命令行工具。但这将不能通过第三方软件调用 Git 。

配置二是 “从命令行以及第三方软件启用 Git” 。该选项被认为是安全的，因为它仅向 PATH 添加了一些最小的 Unix 命令解析器，以避免使用时造成系统环境混乱。您将能够从 Git Bash ，命令提示符和 Windows PowerShell 以及在 PATH 中寻找 Git 或是在任何第三方软件中使用 Git 。这也是推荐的选项。

配置三是 “从命令提示符使用 Git 和可选的 Unix 命令” 。警告：这将覆盖 Windows 命令，如：find 和 sort。你只有在了解其含义后才使用此选项。

一般默认即可。

![img](https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312132154363.webp)

选择[SSH连接](https://link.zhihu.com/?target=https%3A//so.csdn.net/so/search%3Fq%3DSSH%E8%BF%9E%E6%8E%A5%26spm%3D1001.2101.3001.7020)工具

- 选项一是使用内置的 SSH 工具
- 选项二是使用自定义的 SSH 工具

如果没有特殊习惯，默认即可。

![img](https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312132154381.webp)

选择在加密连接时使用的证书

选项一是服务器证书将使用 ca-bundle.crt 文件进行验证。这也是默认的选项。

选项二是“使用本地 Windows 安全通道库”。服务器将使用 Windows 证书验证，此选项还允许您使用公司的内部根 CA 证书，例如使用 Active Directory Domain Services.

一般默认即可

![img](https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312132154351.webp)

配置行尾符号转换

选项一是“查看时使用 Windows 风格的行尾，保存时使用 Unix 风格的行尾”。查看文本文件时，Git 会将 LF 转换为 CRLF 。保存文本文件时， CRLF 将转换为 LF 。对于跨平台项目十分有用，这里是 Windows 上的推荐设置（core.autocrlf设置为true）

选项二是“查看时按原样展示，保存时使用 Unix 样式的行尾”。查看文本文件时，Git 不会执行任何转换。 保存文本文件时，CRLF 将转换为 LF 。对于跨平台项目比较有用，这是 Unix 上的建议设置（core.autocrlf设置为input）

选项三是“查看时按原样展示，保存时按原样保存”。当查看或保存文本文件时，Git 不会执行任何转换。不建议跨平台项目选择此选项（core.autocrlf设置为false）。

一般默认即可。

![img](https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312132154857.webp)

配置终端模拟器以与Git Bash一起使用

选项一是“使用 MinTTY（ MSYS2 的默认终端）”。Git Bash 将使用 MinTTY 作为终端模拟器，该模拟器具有可调整大小的窗口，非矩形文本选择和显示 Unicode 字体。但 Windows 控制台程序（例如交互式 Python ）必须通过“ winpty ”启动才能在 MinTTY 中运行。

选项二是“使用 Windows 的默认控制台窗口”。Git 将使用 Windows 的默认控制台窗口cmd.exe，该窗口可以与 Windows 控制台程序（如交互式 Python 或 node.js ）一起使用，但默认的回滚非常有限，需要配置 Unicode 字体才能正确显示非 ASCII 字符，并且在 Windows 10 之前，其窗口不能自由调整大小，并且只允许矩形文本选择。

一般默认即可。

![img](https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312132154881.webp)

使用git pull命令时默认的模式

一般默认即可。

![img](https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312132154900.webp)

是否启用 `credential helper` 登录凭证管理助手

一般默认即可。

![img](https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312132154913.webp)

配置额外的选项

一般默认即可。

![img](https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312132154015.webp)

是否启用实验功能

这里不勾选，默认选择，如果想尝试新功能，可官网查阅资料了解即可。

![img](https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312132154064.webp)

开始安装，等待片刻，最后finish



![img](https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312132154428.webp)



[引用](https://zhuanlan.zhihu.com/p/597447255)

在你想要操作的文件夹中右键>显示更多选项>

你会看到多出来open git GUI here 和open git Bash here

点击open git Bash here

<img src="https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312132202039.png" alt="image-20231213220238955" style="zoom: 80%;" />

配置用户名和邮箱

```
git config --global user.name "GitHub 用户名"
git config --global user.email "GitHub 邮箱"
```

查询配置

```
git config --global --list
```

### 拉取项目

<a id="拉取项目"></a>

拉取仓库：

```
git clone https://github.com/VNJKDBHJK/WebWork.git
```

其中git@github.com:VNJKDBHJK/WebWork.git，在你想要放的git存储库中找到

<img src="https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312132210814.png" alt="image-20231213220702180" style="zoom:67%;" />

或者

<img src="https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312132210790.png" alt="image-20231213220722795" style="zoom:67%;" />

### 上传-新建仓库

<a id="上传-新建仓库"></a>

在github中新建仓库

<img src="https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312132213575.png" alt="image-20231213221359401" style="zoom:67%;" />

填写仓库信息

(1) 仓库名称，最好是英文+下划线，比如 helloworld、 helloworld_test 

(2) 仓库描述，可选，这里我们填一下，“这是一个学习使用 的仓库”。 

(3) 选择仓库可见性，public 表示你这个项目是开源的，世界 上所有人都可以访问，private 表示私有，只有你或者你允许 的人可以访问，当然后面都是可以变动的，这里我们选择 public。 

(4) Add a README file，这个选项询问你要不要添加一个说 明文件，这个文件就是 github 项目的说明文件，先不管，目 前先不勾选

(5) Add .gitignore, 一般不管，因为在本地创建项目的时候一 般都已经创建好这个文件了，  该文件包含了 Git 应该忽略的文件和文件夹的列表。这些文 件和文件夹不会被提交到版本控制系统中，即使它们在本地 存在。 

(6) Choose a license ，选择开源许可证，如果你的项目要是 public 的，可以选一下开源许可证，以确保你的权利不被侵 犯，当然有好多种许可证，想要了解的可以自行查阅相关资 料，由于目前我们只是学习，并且项目本身没有什么价值， 所以就先不要管这个选项。

 (7) 信息完成后点击 create repository ，创建仓库

创建新仓库指令（本地要上传的文件夹）

```
echo "#test" >> README.md
git init //把这个目录变成Git可以管理的仓库
　　git add README.md //文件添加到仓库
　　git add . //不但可以跟单一文件，还可以跟通配符，更可以跟目录。一个点就把当前目录下所有未追踪的文件全部add了 
　　git branch -m main
　　git commit -m "first commit" //把文件提交到仓库
　　git remote add origin git@github.com:VNJKDBHJK/WebWork.git//关联远程仓库
　　git push -u origin main //把本地库的所有内容推送到远程库上
```

其中

1. `echo "#test" >> README.md`  中`test`为你的本地上传根文件夹名，举例中为test
2. `git remote add origin https://github.com/xxx/xxxx.git`：这 个命令是将远程仓库的 URL 添加到本地 Git 代码库中。这 里的 `origin` 是一个别名，用于代表远程仓库的 URL。你可 以为远程仓库指定不同的别名，但 `origin` 是最常用的别名
3.  `git branch -M main`：这个命令是将本地的默认分支名改 为 `main`。在 Git 2.28 之前，Git 的默认分支名是 `master`， 但为了避免与种族主义相关的词汇，Git 已经决定将默认分 支名改为 `main`
4. ` git push -u origin main `：这个命令是传到 `github` 等远程 仓库，并指定远程分支为 `main` 分支，`git push origin  ` 命令，其中 `` 是你要推 送的分支名
5. 如果是非首次推送，直接输入 `git push` 就可以

例如：

你想把`meiri`推送到库`test`中

<img src="https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312132221221.png" alt="image-20231213222126142" style="zoom: 80%;" />

<img src="https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312132221968.png" alt="image-20231213222144780" style="zoom: 50%;" />

在本地文件夹中右键打开终端`（Windows PowerShell）`

键入：`git init`

复制之后点击右键试试？

<img src="https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312132223329.png" alt="image-20231213222326254" style="zoom:67%;" />

键入`echo "#test" >> README.md`

<img src="https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312132227915.png" alt="image-20231213222732840" style="zoom:67%;" />

键入`git add .`

<img src="https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312132230173.png" alt="image-20231213223011116" style="zoom:67%;" />

很不幸报错了，当你遇到报错时可以看看[git使用中常见报错的解决办法](https://www.cnblogs.com/MrTager/p/12896212.html)

<img src="https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312132231471.png" alt="image-20231213223135390" style="zoom:67%;" />

解决后，键入` git commit -m "first commit"`

<img src="https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312132232136.png" alt="image-20231213223215018" style="zoom:67%;" />

键入`git remote add origin git@github.com:VNJKDBHJK/test.git`

<img src="https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312132234945.png" alt="image-20231213223412841" style="zoom:67%;" />

键入`git push -u origin main`

<img src="https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312132236649.png" alt="image-20231213223652546" style="zoom:67%;" />

不用管上面，直接键入就行

刷新仓库就可以看到推送的文件了

<a id="已有仓库继续上传"></a>

当你新加入了一个文件比如说123.txt希望继续上传

键入`git status`

<img src="https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312132238643.png" alt="image-20231213223852552" style="zoom:67%;" />

看到一个文件未上传

键入`git add 123.txt`

文件多可以`add .`(添加目录下所有文件)

再次`git status`

<img src="https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312132240535.png" alt="image-20231213224045451" style="zoom:67%;" />

提示已加入

键入 `git commit -m “更新说明文件”`（“”中写什么都行）

<img src="https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312132243259.png" alt="image-20231213224345183" style="zoom:67%;" />

键入`git push`

<img src="https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312132244778.png" alt="image-20231213224434555" style="zoom:67%;" />

呕吼，成功加入

ps. 传不上去怎么办？

如果不行，先试试

```
git config --global --unset http.proxy 
git config --global --unset https.proxy
```

再不行，试试
设置>网络和Internet>代理>手动设置代理>编辑>将端口改为代理端口
输入命令

```
git config --global http.proxy http://127.0.0.1:7890（代理端口）
```

检查：

```
git config --global -l
```

再

```
git push -u origin main（不一定是main)
```

