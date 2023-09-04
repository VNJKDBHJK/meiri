# HTML初体验

2023/9/4

<a href="Index.html">自己搓的小网页</a>

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8"></head></meta>
        <title>考考的网页</title>
    </head>
    <body>
        hello 考考
    </body>
</html>
```

```c
<!DOCTYPE html> //档案类型为HTML
    //网站最外层
<html> //开始标签
</html>//关闭标签
    //网页资讯
<head></head>
<meta charset="UTF-8"></head></meta>//使用UTF-8编码方式编码网页->兼容中文
<title>考考的网页</title>//中间夹着的是网页的标题
```

![image-20230904184443837](https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202309041844873.png)

```C
    //网页真正的内容
<body>
        hello 考考
</body>
```

<img src="https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202309041846652.png" alt="image-20230904184630628" style="zoom: 67%;" />

```c
<!--注解-->
```

## 标题及字体

1. 标题

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8"></head></meta>
        <title>考考的网页</title>
    </head>
    <body>
        <!--注解-->
        <h1>h1标题</h1>
        <h2>h2标题</h2>
        <h3>h3标题</h3>
        <h4>h4标题</h4>
        <h5>h5标题</h5>
        <h6>h6标题</h6>
    </body>
</html>
```

<img src="https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202309041926066.png" alt="image-20230904192642027" style="zoom:80%;" />

2. 字体

   ```html
   <!DOCTYPE html>
   <html>
       <head>
           <meta charset="UTF-8"></meta>
           <!--同理上一句也可以写为  <meta charset="UTF-8"/>-->
           <title>考考的网页</title>
       </head>
       <body>
           <!--注解-->
           <h1>h1标题</h1>
   
           <!--br是换行标签,中间不加任何内容-->
           <br></br>
           <!--hr是水平线标签,中间不加任何内容-->
           <hr></hr>
   
           <h2>h2标题</h2>
           <p>这里是内容:
               <br/>
               p标签表示文字和段落
               <br/>
               <b>b标签表示粗体字</b>
               <br/>
               <i>i标签表示斜体字</i>
          </p>
   
           <!--下面这种写法与上面效果一致-->
           <br/>
           <hr/>
   
           <h3>h3标题</h3>
           <h4>h4标题</h4>
           <h5>h5标题</h5>
           <h6>h6标题</h6>
       </body>
   </html>
   ```

   <img src="https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202309041946733.png" alt="image-20230904194605677" style="zoom:80%;" />

   > 当开始和结束标签中间不加东西时,可以将<br></br>简写成为<br/>
   >
   > 

   

## 链接&图片

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8"></meta>
        <!--同理上一句也可以写为  <meta charset="UTF-8"/>-->
        <title>考考的网页</title>
    </head>
    <body>
        <!--a标签需要网址的属性,加href==""-->
        <!--外部网页-->
        <a href="https://www.youtube.com/watch?v=CLUPkcLQm64">html教程网址</a>
        <!--内部网页-->
        <a href="page2.html">第二页</a>
        <!--不在同一文件夹上的网页-->
        <a href="dir/page3.html">第三页</a>

        <!--链接档案-->
        <a href="BACK.gif">背景</a>
        <!--添加图片,后面为链接,(外部网址)-->
        <img src="https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202309042142664.png"/>
        <!--网站自己准备的图片-->
        <img src="6.1.png"/>
        <!--调整照片长宽-->
        <img src="6.1.png" width="960" height="540"/>
        <!--如果只改长或者宽,照片会等比例缩小-->
        <img src="6.1.png" width="960"/>
    </body>
</html>
```

1. 添加链接

   添加链接所用的标签为<a></a>

   该标签添加时需要附上属性

   如:

   + 外部网址

     <a href="https://www.youtube.com/watch?v=CLUPkcLQm64">html教程网址</a>

   + 内部网页

     <a href="page2.html">第二页</a>

   + 不在同一文件夹上的网页

     <a href="dir/page3.html">第三页</a>

   + 链接档案

     <a href="BACK.gif">背景</a>

2. 添加图片

   + 链接图片

     ```
     <img src="https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202309042142664.png"/>
     ```

     

   + 网站自己的图片

     ```
     <img src="6.1.png"/>
     ```

   + 手搓图片长宽

     ```
     <img src="6.1.png" width="960" height="540"/>
     ```

   + 等比例更改图片长宽

     ```
     <img src="6.1.png" width="960"/>
     ```

     
