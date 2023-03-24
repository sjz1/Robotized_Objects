# Height_Measuring_Device



### 작동 원리

낮은 위치에 있는 초음파 센서에 사람이 근접하면 어린이

높은 위치에 있는 초음파 센서에 사람이 근접하면 어른이다라고 인지하는 매커니즘. 


이를 이용해 초음파 센서 2개를 활용해서 adult인지, child 인지 판단합니다.

<img width="80%" src="https://user-images.githubusercontent.com/105138423/218358622-243c381d-9f29-4190-bcee-9a2f2224e6dc.jpg"/>

### 라즈베리파이 장착

ROS 통신에서 rostopic 값을 확인하려고 라즈베리파이 하나를 장착했습니다.
라즈베리파이 sd 카드 안쪽에도 door.py 파일이 있어요.
라즈베리파이 연결된 상태로 원격 제어 후 rosrun 라즈베리파이 안쪽에 있는 파일명 door.py 실행 가능합니다.

이후에 rostopic list로 sensor1, sensor2, height 값 확인 가능합니다.
