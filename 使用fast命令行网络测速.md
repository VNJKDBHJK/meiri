#### 使用fast命令行网络测速

1. 安装FastCLI

   `npm install -g fast-cli`

2. 检测是否成功安装

   `fast --version`

   `npm ls -g --depth=0`

   如果没有显示fast的版本但在npm中存在FastCli版本号，先检查一下有没有安装node.js

   `node --version`

   如果有版本号输出，问题可能没有将fast的路径配置到环境变量内

   一般fast的路径：`C:\Users\你的用户名\AppData\Roaming\npm`

   塞到环境变量里就ok了

3. 测速

   `fast`