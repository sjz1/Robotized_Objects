# Robotized_Objects
![Raspberry Pi](https://img.shields.io/badge/-RaspberryPi-C51A4A?style=for-the-badge&logo=Raspberry-Pi)
<a href="https://www.python.org/">
<img src="https://img.shields.io/static/v1?style=for-the-badge&message=Python&color=3776AB&logo=Python&logoColor=FFFFFF&label="/>
<img src="https://img.shields.io/badge/Android-3DDC84?style=for-the-badge&logo=Android&logoColor=white">
<img src="https://img.shields.io/badge/Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=FFFFFF&label=">
<img src="https://img.shields.io/badge/ROS-22314E?style=for-the-badge&logo=ROS&logoColor=FFFFFF&label=">
</a><br/>
<!-- <img src="https://img.shields.io/badge/표시할이름-색상?style=for-the-badge&logo=기술스택아이콘&logoColor=white"> -->


<img src="https://cdn.hellodd.com/news/photo/202301/99326_316754_2030.gif" width="480" height="270">

<br/><br/>

## **Index**
>###  [1. Press Release](#1-press-release)
>###  [2. Introduce](#introduce)
>> ###  [2-1 child scenario](#case-of-child)
>> ### [2-2 adult scenario](#case-of-adult)
>###  [3. Detail for config code](#detail-for-config-code)
>###  [4. Collabot-project-branch-guide](#collabot-project-branch-guide)

<br/><br/>


# Press Release
>#### **[YTN 사이언스]** [스스로 책장이 움직이는 로보틱 도서관 시스템 개발](https://science.ytn.co.kr/program/view.php?mcd=0082&hcd=&key=202301191652323862)

>#### **[디지털조선일보]** [현실로 등장한 해리포터 속 ‘마법 도서관’](https://digitalchosun.dizzo.com/site/data/html_dir/2023/01/19/2023011980233.html) 

>#### **[MBC 뉴스데스크]** ["책 여기 있어요~" 일상으로 스며든 로봇 기술](https://imnews.imbc.com/replay/2023/nwdesk/article/6447885_36199.html)

>#### **[YTN 뉴스]** [도서관에 웬 로봇?!...와우, 열 일 하네!](https://www.ytn.co.kr/_ln/0105_202301220543400486)

>#### [**[조선비즈]** [도서관 서가와 의자가 도우미 로봇으로 변신하다](https://zdnet.co.kr/view/?no=20230119130733)

>#### [**[연합뉴스]** [도서관 책장이 저절로 움직인다…KIST, 로보틱 시스템 개발](https://www.yna.co.kr/view/AKR20230119080100017?input=1195m)

>#### **[동아사이언스]** [서고의 책을 고르자 로봇이 반응했다](https://www.dongascience.com/news.php?idx=58108)

>#### **[헤럴드경제]** [KIST, 스스로 책 꺼내는 ‘로보틱 도서관’ 개발](http://news.heraldcorp.com/view.php?ud=20230120000341)

>#### **[파이낸셜뉴스]** [서재·도서관 전체가 거대 로봇이 됐다](https://www.fnnews.com/news/202301191437173711)

>#### **[전자신문]** [KIST, 소셜로봇의 새로운 패러다임 제시](https://www.etnews.com/20230119000248)

>#### **[로봇신문]** [KIST, 로보틱 도서관 '콜래봇'으로 국제로봇 디자인 대회 최고상 수상](http://www.irobotnews.com/news/articleView.html?idxno=30596)

>#### **[아시아경제]** ["온 집안 연결해 뭐든 다 도와"…로봇의 개념 바뀐다](https://view.asiae.co.kr/article/2023011911035324632)

>#### **[충청뉴스]** [KIST ‘콜래봇’ ICSR 2022서 최고상 수상](http://www.ccnnews.co.kr/news/articleView.html?idxno=282845)

>#### **[헤럴드경제]** [“휴대폰 검색하면 원하는 책이 자동 돌출”…똑똑한 로보틱 도서관 등장](http://news.heraldcorp.com/view.php?ud=20230119000436)

>#### **[정보통신신문]** [KIST 콜래봇, ICSR 2022 최고상 수상](http://www.koit.co.kr/news/articleView.html?idxno=108634)

>#### **[워크투데이]** [KIST '콜래봇', 소셜로봇의 새로운 패러다임 제시하다](http://www.worktoday.co.kr/news/articleView.html?idxno=31925)

>#### **[헬로디디]** [검색한 책 알아서 꺼내주는 도서관?···소셜로봇 패러다임 '격변'](https://www.hellodd.com/news/articleView.html?idxno=99326)



<br/><br/>





# Introduce
Let me introduce about Robotized_Objects Structure.<br/><br/>

>**catkin_ws1** -> workspace for collabot<br/>
>**catkin_ws1/bag/test3.bag** -> recording bag file to test the scenario<br/>
>**catkin_ws1/src/az_body_tracker/** -> Directory fro using Azure Camera<br/>

</br>

### **Divide a scenario into two cases with adult/child**
---
### **Case of Child**<br/>

#### Launch File for **child scenario**.<br/>
>please run **"catkin_ws1/src/collabot_ver1/child_collabot_ver1.launch"**<br/>
or <br/>
>**"./child_collabot_ver1.launch"**
>```bash
>roslaunch collabot_ver1 child_collabot_ver1.launch
>```
>catkin_ws1/src/collabot_ver1/child_collabot_ver1.launch : Launch File for **child scenario**.<br/>

<br/>

### **Case of Adult**<br/>
 #### Launch File for **adult scenario**.<br/>
>please run **"catkin_ws1/src/collabot_ver1/adult_collabot_ver1.launch"**<br/>
>or <br/>
>**"./adult_collabot_ver1.launch"**
>```bash
>roslaunch collabot_ver1 adult_collabot_ver1.launch
>```
<br/>

### **"Add) If you want to switch adult/chind with height threshold**<br/>
>open the **"./collabot_ver1.launch"** with Text Editer and change Threshold (default : 800)
>```bash
>nano collabot_ver1.launch 
>roslaunch collabot_ver1 collabot_ver1.launch
>```

<br/><br/>

# Directories Structure <br/>
```bash
Robotized_Objects
┣ bag
┃ ┗ test.bag
┃
┣ config
┃   ┣ ac_pub_az_sub.py
┃   ┣ motor_publish_ver1.ino
┃   ┗ sceinaro_make.py
┃
┣ sample
┃   ┣ img
┃   ┗ video
┃
┣ utils
┃   ┣ ssim
┃   ┃ ┣ get_ROI.py
┃   ┃ ┣ grad_ssim_graph.py
┃   ┃ ┣ make_sample_video.py
┃   ┃ ┣ ssim_graph.py
┃   ┃ ┗ ssim_play.py
┃   ┃ 
┃   ┣ monitor.py
┃   ┗ print_monitor.py
┃
┗ catkin_ws1
  ┣ build
  ┣ devel
  ┗ src
     ┣ 🎁 az_body_tracker
     ┃    ┣ cmake
     ┃    ┣ include
     ┃    ┣ launch
     ┃    ┣ src
     ┃    ┃  ┣ az_body_tracker.cpp
     ┃    ┃  ┗ TrackerNode.cpp
     ┃    ┗ window_controller_3d
     ┗ 🎁 collabot_ver1
          ┣ adult_collabot_ver1.launch
          ┣ child_collabot_ver1.launch
          ┣ CMakeLists.txt
          ┣ collabot_ver1.launch
          ┗ src
             ┣ ac_pub_az_sub.py
             ┣ monitor.py
             ┣ print_monitor.py
             ┣ motor_publish_ver1.ino
             ┗ sceinaro_make.py
```

</br></br>


# Detail for config code<br/>
### **catkin_ws1/src/collabot_ver1/src/ac_pub_az_sub.py**  | **config/ac_pub_az_sub.py**: <br/>
>Subscribe the information of Azure & publish adult/child topic<br/>

<br/>

### **catkin_ws1/src/collabot_ver1/src/monitor.py | utils/moitor.py**  
>Custom Monitoring Code For Exhibition (same as print_monitor.py)<br/>

<br/>

### **catkin_ws1/src/collabot_ver1/src/motor_publish_ver1.ino | config/motor_publish_ver1.ino**
>Publish the # of bookcase(touched via APP) and # of opening bookcase  count from OpenCR behind the bookcase<br/>

<br/>

### **catkin_ws1/src/collabot_ver1/src/sceinaro_make.py**
>Publish the Scenario Using Subscribing informations (adult/child ,count, bookcase_num)

<br/><br/>


# Collabot project Branch Guide <br/>
### **Branch index**

* [1. beginner-branch](#1-beginner-branch)<br/>
* [2. dynamixel check branch](#2-dynamixel_check-branch)<br/>
* [3. raspberrypi_setting branch](#3-raspberrypi_setting-branch)<br/>
* [4. height_measuring branch](#4-height_measuring-branch)<br/>
* [5. frontend branch](#5-frontend-branch)<br/>
* [6. bookcase branch](#6-bookcase-branch)<br/>
* [7. image_difference branch](#7-image_difference-branch)<br/>

[]()<br/>

### 1. Beginner branch

#### If you attend this project at First, Please checkout the Beginner Branch <br/>


https://github.com/sjz1/Robotized_Objects/tree/beginner <br/>


```bash
git checkout beginner
```


### 2. Dynamixel_Check branch
This Branch target to test Dynamixel from local setting

https://github.com/sjz1/Robotized_Objects/tree/Dynamixel_Check <br/>


```bash
git checkout Dynamixel_Check
```


### 3. RaspberryPi_Setting branch
This Branch target to introduce "How to setting RasberryPI for our environment"

https://github.com/sjz1/Robotized_Objects/tree/RasberryPi_Setting <br/>


```bash
git checkout RaspberryPi_Setting
```

### 4. Height_Measuring  branch
This Branch target to introduce "How to measure Person's Height using Ultrasonic Sensor"

https://github.com/sjz1/Robotized_Objects/tree/Height_Measuring  <br/>


```bash
git checkout Height_Measuring 
```


### 5. Frontend  branch
Build App by using Appinventor

https://github.com/sjz1/Robotized_Objects/tree/Frontend  <br/>


```bash
git checkout Frontend
```


### 6. Desk  branch
This Branch for "Desk" part

https://github.com/sjz1/Robotized_Objects/tree/Desk  <br/>


```bash
git checkout Desk
```


### 6. Bookcase  branch
This Branch for "Bookcase" part

https://github.com/sjz1/Robotized_Objects/tree/Bookcase  <br/>


```bash
git checkout Bookcase
```


### 7. Image_Difference  branch
This Branch for "Image_Difference" part
Use to Decide whether or not User Picking up books 

https://github.com/sjz1/Robotized_Objects/tree/BookcImage_Difference  <br/>


```bash
git checkout Image_Difference
```


 <br/> <br/>
