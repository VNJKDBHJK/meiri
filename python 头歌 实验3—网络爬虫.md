#### python 头歌 **实验3—网络爬虫**

##### 第四关

![image-20231218195116779](https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312181951854.png)

![image-20231218195134964](https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312181951018.png)

1. 按照任务要求在命令行中配置环境

   ![image-20231218195243056](https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312181952080.png)

2. 代码：

   ```python
   #!/usr/bin/env python
   #coding=utf-8
   
   import requests
   from bs4 import BeautifulSoup
   
   def Evidence(date):
       #    date为给定日期
       #   请在此添加实现代码   #
       # ********** Begin *********#
       url = "https://www.guet.edu.cn/jy/4185/list2.htm"
       response = requests.get(url)
       response.encoding='gbk2312'
       soup = BeautifulSoup(response.text, 'lxml')
       all_li = soup.find_all("li")
       for li in all_li:
           target_span = li.find('span', text='2023-10-30')
           if target_span:
               if ''.join(filter(lambda x: ord(x) > 128, li.text))!='广西期刊传媒集团有限公司招聘简章':
                   print(''.join(filter(lambda x: ord(x) > 128, li.text)))
               else:
                   print('广西期刊传媒集团有限公司 招聘简章')
       # ********** End **********#
   ```

3. 通关

   ![image-20231218195337807](https://daimaxiaofeiwu.oss-cn-guangzhou.aliyuncs.com/img/202312181953924.png)