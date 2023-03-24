# RaspberryPi_Setting

### 새 터미널
roscore


### 새 터미널 
ssh ubuntu@ 라즈베리파이 ip


### 라즈베리파이를 처음 세팅하는 법  (os 설치부터 )
1. sd 카드를 리더기에 넣고 노트북 or PC에 꽂아야 함. (무난하게 16gb 이상)


2. 우분투 OS를 다운받기, 
(https://emanual.robotis.com/docs/en/platform/turtlebot3/sbc_setup/#sbc-setup) 혹은 우분투 홈페이지에서 server-64 파일을 받으면 됨.


3. imager 프로그램 실행. 노트북에 sd카드를 꽂아두기. 


4. imager 내 '사용자 정의 사용'에서 다운받은 우분투 os 파일을 선택하고, sd 카드 저장소를 선택. 쓰기로 os를 받아주기. 

- Disks Utility, Resize the Partition 부분은 
(https://emanual.robotis.com/docs/en/platform/turtlebot3/sbc_setup/#sbc-setup)
에서 가능.
본인은 Resize the Partition만 했음.


5. 이 때 sd 카드를 다시 노트북에 재접속해주고 


6. PC 내 터미널을 켜주고 (Ctrl+Alt+T)
```
cd /media/$USER/writable/etc/netplan
```
입력 ($USER는 노트북의 pc 사용자 이름을 뜻하는데 제가 썼을 때는 kist)


7. 

```
sudo nano 50-cloud-init.yaml 
```
(이게 우분투 공식 홈페이지에서는 네트워크 파일 이름이 달라질 수 있습니다. 
ls는 해당 directory의 패키지들을 볼 수 있으니 해당 파일 명을 검색하시면 됩니다.)




와이파이에서 원하는 와이파이와 패스워드를 줍니다. 
적용이 완료되었으면 모니터로 연결해서 확인 가능.

처음 모니터에 연결하고 로그인창이 뜨면
```
ID: ubuntu
PW: ubuntu or turtlebot 
```
turtlebot emanual 사이트에서 os를 받았으면 turtlebot이고, 
ubuntu 공식 사이트에서 받았으면 ubuntu 혹은 raspberrypi. 비밀번호 인증 안되면 구글링 필수



### 라즈베리파이 ip 변경하는 법  

1. sd카드를 뽑아서 모니터에 연결. (라즈베리파이3 전원은 마이크로5핀, 라즈베리파이4 전원은 usb-c타입)


2. 모니터에 먼저 HDMI 선을 연결한 상태로 라즈베리파이 전원을 연결.


3. 모니터에 라즈베리파이 화면이 나오고 로그인.
```
ID: ubuntu
PW: 0000kist, turtlebot, kist 중 하나
```

4. 터미널을 열고 (ctrl+alt+T) 


5. 

```
ifconfig
```

ip를 확인.


6. 
```
sudo nano ~/.bashrc 
```

여기에서 

```
export ROS_MASTER_URI=http://{IP_ADDRESS_OF_REMOTE_PC}:11311
export ROS_HOSTNAME={IP_ADDRESS_OF_RASPBERRY_PI_3}
```
이 보일 건데 
```
export ROS_MASTER_URI=http://pc 혹은 노트북 ip를 뜻함:11311
export ROS_HOSTNAME=라즈베리파이 ip를 뜻함
```
pc와 라즈베리파이 각각 ifconfig로 ip를 확인해준 후

ctrl+x로 닫아주고, 수정한 상태로 닫을거냐고 영어로 나오는데 y를 눌러줍니다.  


7. 
```
source ~/.bashrc
```

를 꼭 해주어야 함.  <br/> <br/>


해당 방법은 모두 
(https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/)
에 있으며 한글 말로 풀어두었습니다. 
그리고 자잘한 오류가 있다면 사소한 과정 하나를 빼먹어서 생겼을 가능성이 높고, 이건 구글링으로 직접 찾아보며 해결하는 것이 좋습니다. 


추가로 ROS나 네트워크 세팅에 관한 정리는
https://aisj.tistory.com/140 에서 확인 가능합니다 
