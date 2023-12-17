# typora一些奇妙的小配置

[TOC]

## 点击在页面内跳转：

### 锚点跳转

```
<a id="基本公式"></a>
```

设置锚点

```
<a href="#基本公式">2-14，2-15</a>
```

跳转到锚点

[引用](https://blog.csdn.net/qq_41907769/article/details/121722716)

### 悬浮跳转

为typora添加悬浮实现顶部/底部跳转

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

## 改变字体颜色

改变字体颜色

使用公式进行修改：

```
输入$，按Esc键会自动在后面加上一个$，然后在这两个$之间输入公式。
	     样式如下：
——>	     $\textcolor{red}{这里输入你要改变颜色的文字}$
```

颜色公式：

```
$\textcolor{GreenYellow}{GreenYellow} $
$\textcolor{Yellow}{Yellow}$
$\textcolor{Goldenrod}{Goldenrod} $
$\textcolor{Dandelion}{Dandelion}$
$\textcolor{Apricot}{Apricot} $
$\textcolor{Peach}{Peach}$
$\textcolor{Melon}{Melon} $
$\textcolor{YellowOrange}{YellowOrange}$
$\textcolor{Orange}{Orange} $
$\textcolor{BurntOrange}{BurntOrange}$
$\textcolor{Bittersweet}{Bittersweet}$
$\textcolor{RedOrange}{RedOrange} $
$\textcolor{Mahogany}{Mahogany}$
$\textcolor{Maroon}{Maroon} $
$\textcolor{BrickRed}{BrickRed}$
$\textcolor{Red}{Red} $
$\textcolor{OrangeRed}{OrangeRed}$
$\textcolor{RubineRed}{RubineRed}$
$\textcolor{WildStrawberry}{WildStrawberry}$
$\textcolor{Salmon}{Salmon}$
$\textcolor{CarnationPink}{CarnationPink}$
$\textcolor{Magenta}{Magenta} $
$\textcolor{VioletRed}{VioletRed}$
$\textcolor{Rhodamine}{Rhodamine} $
$\textcolor{Mulberry}{Mulberry}$
$\textcolor{RedViolet}{RedViolet} $
$\textcolor{Fuchsia}{Fuchsia}$
$\textcolor{Lavender}{Lavender} $
$\textcolor{Thistle}{Thistle}$
$\textcolor{Orchid}{Orchid} $
$\textcolor{DarkOrchid}{DarkOrchid}$
$\textcolor{Purple}{Purple} $
$\textcolor{Plum}{Plum}$
$\textcolor{Violet}{Violet} $
$\textcolor{RoyalPurple}{RoyalPurple}$
$\textcolor{BlueViolet}{BlueViolet}$
$\textcolor{Periwinkle}{Periwinkle}$
$\textcolor{CadetBlue}{CadetBlue}$
$\textcolor{CornflowerBlue}{CornflowerBlue}$
$\textcolor{MidnightBlue}{MidnightBlue}$
$\textcolor{NavyBlue}{NavyBlue} $
$\textcolor{RoyalBlue}{RoyalBlue}$
$\textcolor{Blue}{Blue} $
$\textcolor{Cerulean}{Cerulean}$
$\textcolor{Cyan}{Cyan} $
$\textcolor{ProcessBlue}{ProcessBlue}$
$\textcolor{SkyBlue}{SkyBlue} $
$\textcolor{Turquoise}{Turquoise}$
$\textcolor{TealBlue}{TealBlue} $
$\textcolor{Aquamarine}{Aquamarine}$
$\textcolor{BlueGreen}{BlueGreen} $
$\textcolor{Emerald}{Emerald}$
$\textcolor{JungleGreen}{JungleGreen}$
$\textcolor{SeaGreen}{SeaGreen} $
$\textcolor{Green}{Green}$
$\textcolor{ForestGreen}{ForestGreen}$
$\textcolor{PineGreen}{PineGreen} $
$\textcolor{LimeGreen}{LimeGreen}$
$\textcolor{YellowGreen}{YellowGreen}$
$\textcolor{SpringGreen}{SpringGreen}$
$\textcolor{OliveGreen}{OliveGreen}$
$\textcolor{RawSienna}{RawSienna} $
$\textcolor{Sepia}{Sepia}$
$\textcolor{Brown}{Brown} $
$\textcolor{Tan}{Tan}$
$\textcolor{Gray}{Gray} $
$\textcolor{Black}{Black}$
```

[引用](https://blog.csdn.net/liulei952413829/article/details/114670380)

## 打出表情（emoji)

使用:emoji:的形式来打出 emoji

![image-20231217121947239](https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312171219273.png)

:orange:

:green_apple:

:apple:

:pear:

:banana:

:peach:

:pineapple:

:strawberry:

:grapes:

## 使用脚注

在插入脚注位置后加上

```
[^ number ]
```

在说明处加上

```
[^ number ]:内容
```

举例：

引用[^ 1 ]

[^ 1 ]:https://sspai.com/post/54912

> shift + F12 检查元素（与浏览器一致）

## YAML front-matter

[贴个网址](https://hexo.io/zh-cn/docs/themes)

## 遇到问题

### 遇到格式乱换行问题

打开github发现

![image-20231217134114260](https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312171341433.png)

完全乱掉只能看原码

![image-20231217134142020](https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312171341098.png)

一开始我在每行后都加了`<br/>`

![image-20231217134807865](https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312171348911.png)

![image-20231217134825986](https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312171348044.png)

但这也太麻烦了，远不如直接换行的方便

引用[^ 1 ]从这篇文章扒下来一点东西

- **软换行：**需要说明的是，在 Markdown 语法中，换行（line break）与换段是不同的。且换行分为软换行和硬换行。在 Typora 中，你可以通过 `Shift + Enter` 完成一次软换行。软换行只在编辑界面可见，当文档被导出时换行会被省略。
- **硬换行：**你可以通过 `空格 + 空格 + Shift + Enter` 完成一次硬换行，而这也是许多 Markdown 编辑器所原生支持的。硬换行在文档被导出时将被保留，且没有换段的段后距。
- **换段：**你可以通过 `Enter` 完成一次换段。Typora 会自动帮你完成两次 `Shift + Enter` 的软换行，从而完成一次换段。这也意味着在 Markdown 语法下，换段是通过在段与段之间加入空行来实现的。

<img src="https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312171350565.png" alt="image-20231217135011522"  />

![image-20231217135107035](https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312171351117.png)

ok了，完全ok

。。。后续会增加

好吧或许会日更。

