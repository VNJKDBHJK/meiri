# git配置（自用）

git下载包已存在。。。[git下载](https://www.git-scm.com/download/)
设置用户名和邮箱
git config --global user.name "GitHub 用户名"
git config --global user.email "GitHub 邮箱"
没了。

创建新仓库指令
git init //把这个目录变成Git可以管理的仓库
　　git add README.md //文件添加到仓库
　　git add . //不但可以跟单一文件，还可以跟通配符，更可以跟目录。一个点就把当前目录下所有未追踪的文件全部add了 
　　git commit -m "first commit" //把文件提交到仓库
　　git remote add origin git@github.com:wangjiax9/practice.git //关联远程仓库
　　git push -u origin master //把本地库的所有内容推送到远程库上

如果不行，先试试
git config --global --unset http.proxy 
git config --global --unset https.proxy
再不行，试试
设置>网络和Internet>代理>手动设置代理>编辑>将端口改为代理端口
输入命令
git config --global http.proxy http://127.0.0.1:7890（代理端口）
检查：git config --global -l
再
git push -u origin main（不一定是main)

