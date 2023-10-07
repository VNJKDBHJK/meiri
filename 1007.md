# java初体验

1. JVM: java virtual machine: java虚拟机,真正运行java程序的地方

2. 核心类库: java自己写好的程序,给程序员自己的程序调用的

3. JRE: java runtime environment : java的运行环境

4. JDK: java development kit: java开发工具包

   <img src="https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202309291606603.png" alt="image-20230929160614458" style="zoom: 50%;" />

5. 编写简单程序

   <img src="https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202309291608138.png" alt="image-20230929160817076" style="zoom:50%;" />

   大概步骤

6. java跨平台,可以在各种安装JVM的系统上运行

7. Path环境变量 

   > 在命令行窗口启动任意程序

   1. 在系统中找到高级系统设置,点击环境变量查找path变量

      <img src="../AppData/Roaming/Typora/typora-user-images/image-20231007194116871.png" alt="image-20231007194116871" style="zoom:67%;" />

   2. 双击path后新建

      <img src="https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202310071942740.png" alt="image-20231007194213703" style="zoom:67%;" />

   3. 将exe文件的路径复制粘贴进去,点击确定

      ![image-20231007194317429](https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202310071943513.png)

   4. 后打开命令行窗口,直接输入名字,例如qq

      ![image-20231007194504321](https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202310071945382.png)

8. 配置java和javac的环境变量

   找到java的bin包,配置到系统或者用户变量中去,删除系统自动配置的java将复制好的路径按照上面的方式配置环境变量

9. 配置java_home环境变量

   找到java_home

   ![image-20231007195532823](https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202310071955872.png)

   找到这段路径,

   ![image-20231007195610314](https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202310071956350.png)

   进入环境变量后新建,输入变量名称与刚刚复制的路径

10. 可以更改path中java的路径为%Java_Home%\bin

    ![image-20231007200256954](https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202310072002990.png)

    与之前效果是一样的

    2023.10.7