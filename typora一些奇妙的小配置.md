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

3. 改变字体颜色

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

3. 

。。。后续会增加

好吧或许会日更。