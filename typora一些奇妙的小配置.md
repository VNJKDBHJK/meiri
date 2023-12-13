# typora一些奇妙的小配置

## 点击在页面内跳转：

1. ```
   <a id="基本公式"></a>
   ```

   设置锚点

   ```
   <a href="#基本公式">2-14，2-15</a>
   ```

   跳转到锚点

[引用](https://blog.csdn.net/qq_41907769/article/details/121722716)

2. 为typora添加悬浮实现顶部/底部跳转

   找到：typora(安装目录)>resources>window.html

   查找id=“write”行代码替换为

   ```
   <div id="write" class="ty-before-first-render" contenteditable="false" spellcheck="true" tabindex="-1"><div style="opacity: 0"><h1>ABCDEFG</h1><p>abcdefg</p></div></div>
   ```

   ![image-20231213100718826](https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312131007014.png)

   在这一行的上方添加置顶

   ```
   <a id='SHH' ></a>
   ```

   在这一行的下方添加置底

   ```
   <a id='DD' ></a>
   ```

   在置底后添加

   ```
   <a id="HeadStart" href="#SHH" style="display: inline-block;width: 70px;border-radius: 50%;position: fixed;bottom: 13%;right: 5%; text-decoration: none;font-size: 20px; color: #77ac98; z-index:1" >▲</a><a id="down" href="#DD" style="display: inline-block;width: 70px;border-radius: 50%;position: fixed;bottom: 10%;right: 5%; text-decoration: none;font-size: 20px; color: #77ac98; z-index:1" >▼</a>
   
   ```

   出现

   ![image-20231213100929597](https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312131009620.png)

   [引用](https://blog.csdn.net/m0_58311262/article/details/130524658)

3. 

。。。后续会增加