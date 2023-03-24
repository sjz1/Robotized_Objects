
<img width="80%" src="https://user-images.githubusercontent.com/105138423/218000713-29d18508-56b7-44db-90d1-57a6d339cee3.jpg"/>

# Robotized_Bookcase


### 1. 모터 처음 작동시킬 때

높은 전압을 요구하므로 마이크로5핀 외에 (리눅스 기준 /dev/ttyACM0 경로) 모터 전원선 혹은 배터리를 연결해야 합니다. 


### 2. 모터 번호 설정 

처음 모터를 구매하면 id값이 1로 존재하므로 openCR 보드에서 id를 scan해준 후 id_change 예제로 변환해야 합니다. 
아두이노-예제-openCR-Dynamixel Workbench 경로에서 확인하실 수 있습니다. 


### 3. 처음 노트북에 openCR 보드를 세팅
<img width="80%" src="https://user-images.githubusercontent.com/105138423/218001682-4e4eec98-e530-4a6e-9624-e5648a24bcf3.PNG"/>
아두이노-환경설정 에서 
(https://raw.githubusercontent.com/ROBOTIS-GIT/OpenCR/master/arduino/opencr_release/package_opencr_index.json) 복사 붙여넣기로 추가해줍니다. 
그 다음 board manager에서 openCR 다운 받아주고, Library Manager에서 dynamixel 관련 라이브러리 다운 받아주어야 합니다. 


### 4. 포트 문제 발생시 

(https://emanual.robotis.com/docs/en/software/arduino_ide/)
에서 찾아보면 됩니다.
포트 인식이 안될 경우 
```
sudo chmod 666 /dev/ttyACM0
```
로 권한 부여가 안된 상태거나 
```
sudo usermod -a -G dialout $USER 
```
후 다시 해주면 해결 됩니다. 

그것도 안되면 openCR emanual로 가서 펌웨어 확인.

소프트웨어 문제가 아니라면 하드웨어를 확인해보고 새로운 걸로 바꾸기. 


### 5. 코드 
<img width="80%" src="https://user-images.githubusercontent.com/105138423/218001887-51d7dea0-ffe2-4a2e-a711-54ab863b6d52.PNG"/>
다이나믹셀 baudrate는 57600으로 고정. openCR workbench 참고 
(https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_workbench/)
```
int motor_open[5] = {0,};
int sensor_on[5] = {0,};
int stack[5] = {0,};
```

초음파 센서 관련된 함수. motor_open은 모터가 작동될 때 트리거 역할을 하는 변수이고, sensor on은 초음파 센서가 측정하도록 활성화하는 트리거 역할,
stack은 일정 stack이 쌓이면 motor_open을 0으로 만들어 서랍을 닫히게 하는 역할을 합니다.
이 때 delay를 쓰지 않고 stack이라는 특정 변수가 더하는 값으로 만들어졌기 때문에 닫히는 타이밍은 반복적인 실험을 통해 확정하였습니다. 

```
Serial.begin(9600);
Serial2.begin(9600);
```
serial.begin은 시리얼 모니터 통신용이고 serial2 begin은 uart 포트 통신용.

```
dxl_wb.init(DEVICE_NAME, BAUDRATE, &log); 
```
모터 초기 세팅 

```
dxl_wb.ping(motor[모터번호], &model_number, &log);  
```
모터 번호에 맞게 모터 추가.
```
dxl_wb.setExtendedPositionControlMode(motor[모터 번호], &log); 
```
모터 포지션 컨트롤 모드. 이것도 다이나믹셀 emanual api reference에 있는데 
여러 함수가 있음. setExtendedPositionControlMode은 1번 이상으로 position 이동이 가능. 
속도 제어보다 포지션 이동이 정확한 모터 구동이 되서 사용 중.
```
dxl_wb.getPresentPositionData(motor[모터번호], &presentposition[모터번호], &log);
```
현재 위치를 지정해주는 거. 그래서 처음 서랍 위치를 잘 맞추는게 중요. 열린 상태로 처음 위치를 지정하면 레일하고 벨트 부분 망가집니다.


-----------------------------------------------------------------------------------------------------------
### 책장 설계 부분 

(https://github.com/juhan0910/CollaBot_3D_CAD)
두번째 책장 부분은 이전 프로젝트에서 제 onshape 문서로 작업하여 공유하였습니다. 
위 github 링크로 올렸으니 참고 바랍니다. 







각 3d 프린터 출력물마다 용도는 다음과 같습니다. 

Motor support 430: 430 모터에 결합

(Motor) down support: 540 모터에 결합

GT2 pulley motor 430: GT2라는 벨트에 결합 (모터 430 있는 쪽)

GT2 Clamp: 430 클램프 박는 용도 

Ultrasonic sensor cover: 초음파 센서 커버 (서랍에 붙였던 거))

Ultrasonic sensor stick: 초음파 센서 뒤에서 꽂는 거. 

Shaft Cover: shaft hole 달고 pulley 달고 그 다음 마지막으로 뚜껑으로 덮는 용도 -> 위 아래 서랍 공통

Down shaft 4 hole: 책장 가장 아래 단 듯

GT2 pulley (motor):  540 아래쪽 모터 달 때 씀 

GT2 Pulley: Shaft hole 연결할 때 쓰는 거. 

540하고 430 모터 제어는 동일 (emanual 참고) 
프로파일 할 때 미리 사각 너트를 딱 맞게 넣고 그 다음 프로파일을 결합할 것



처음 보셨을 때 어려울 수도 있겠지만 책장 조립에 썼던 3D 프린팅 출력물과 onshape 출력물을 비교하시면서 공부하면 됩니다.

혹시 상용화된 제품(서보모터나 바퀴, 기어 등)을 Onshape로 불러오고 싶다면 grabcad 사이트에서 부품을 검색하시면 됩니다. 


------------------------------------------------------------------------------------------------------------

### 미니어처 책장
책장은 아두이노 우노 보드 같은 경우에는 UTP선과 보드를 납땜하였고,
열고자 하는 서랍 부분만 미리 홈을 내어 서보모터를 달았습니다. 

코드는 스위치 라이브러리 다운 받아주시고 업로드 해주셔야 합니다.

서보모터가 한쪽만 연결되어 있기 때문에 모멘트를 받아서 구동할 때 서랍이 덜컹 거리고 움직이지 않을 수가 있습니다. 
그래서 3D 프린터로 서랍 모양의 출력물을 만들 때 맞은 편 면에 지지대를 하나 만들었습니다. 


