#include <DynamixelWorkbench.h>

#if defined(__OPENCM904__)
#define DEVICE_NAME "3" //Dynamixel on Serial3(USART3)  <-OpenCM 485EXP
#elif defined(__OPENCR__)
#define DEVICE_NAME ""
#endif

#define BAUDRATE  57600

#define MOTOR1  1
#define MOTOR2  2
#define MOTOR3  3
#define MOTOR4  4
#define MOTOR5  5
#define MOTOR6  6
#define MOTOR7  7
#define MOTOR8  8
#define MOTOR9  9
#define MOTOR10 10
#define MOTOR11 11
#define MOTOR12 12

DynamixelWorkbench dxl_wb;

int motor_open[10] = {0,};
int sensor_on[10] = {0,};
int stack[10] = {0,};

uint16_t model_number = 0;
int32_t presentposition[13];
int initial_pos[13] = {0,};
int initial_5 = 0;
int initial_6 = 0;
int initial_7 = 0;
int initial_8 = 0;
int initial_9 = 0;
int initial_10 = 0;
int initial_11 = 0;
int initial_12 = 0;
uint8_t motor[13] = {0, MOTOR1, MOTOR2, MOTOR3, MOTOR4, MOTOR5, MOTOR6, MOTOR7, MOTOR8, MOTOR9, MOTOR10, MOTOR11, MOTOR12};

const int trigPin[5] = {50, 52, 54, 58, 56};
const int echoPin[5] = {51, 53, 55, 59, 57};

long duration[5] = {0,};
float distance[5] = {0,};

float Distance_sensing(int i) {

  digitalWrite(trigPin[i], LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin[i], HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin[i], LOW);
  duration[i] = pulseIn(echoPin[i], HIGH);
  return duration[i] * 0.034 / 2;

}

void setup() {

  pinMode(trigPin[0], OUTPUT);
  pinMode(echoPin[0], INPUT);
  pinMode(trigPin[1], OUTPUT);
  pinMode(echoPin[1], INPUT);
  pinMode(trigPin[2], OUTPUT);
  pinMode(echoPin[2], INPUT);
  pinMode(trigPin[3], OUTPUT);
  pinMode(echoPin[3], INPUT);
  pinMode(trigPin[4], OUTPUT);
  pinMode(echoPin[4], INPUT);

  Serial.begin(9600);
  Serial2.begin(9600);
}

void loop() {

  const char *log;
  dxl_wb.init(DEVICE_NAME, BAUDRATE, &log);

  dxl_wb.ping(motor[5], &model_number, &log);
  dxl_wb.ping(motor[6], &model_number, &log);
  dxl_wb.ping(motor[7], &model_number, &log);
  dxl_wb.ping(motor[8], &model_number, &log);
  dxl_wb.ping(motor[9], &model_number, &log);
  dxl_wb.ping(motor[10], &model_number, &log);
  dxl_wb.ping(motor[11], &model_number, &log);
  dxl_wb.ping(motor[12], &model_number, &log);

  dxl_wb.setExtendedPositionControlMode(motor[5], &log);
  dxl_wb.setExtendedPositionControlMode(motor[6], &log);
  dxl_wb.setExtendedPositionControlMode(motor[7], &log);
  dxl_wb.setExtendedPositionControlMode(motor[8], &log);
  dxl_wb.setExtendedPositionControlMode(motor[9], &log);
  dxl_wb.setExtendedPositionControlMode(motor[10], &log);
  dxl_wb.setExtendedPositionControlMode(motor[11], &log);
  dxl_wb.setExtendedPositionControlMode(motor[12], &log);

  dxl_wb.torqueOn(motor[5], &log);
  dxl_wb.torqueOn(motor[6], &log);
  dxl_wb.torqueOn(motor[7], &log);
  dxl_wb.torqueOn(motor[8], &log);
  dxl_wb.torqueOn(motor[9], &log);
  dxl_wb.torqueOn(motor[10], &log);
  dxl_wb.torqueOn(motor[11], &log);
  dxl_wb.torqueOn(motor[12], &log);

  dxl_wb.getPresentPositionData(motor[5], &presentposition[5], &log);
  dxl_wb.getPresentPositionData(motor[6], &presentposition[6], &log);
  dxl_wb.getPresentPositionData(motor[7], &presentposition[7], &log);
  dxl_wb.getPresentPositionData(motor[8], &presentposition[8], &log);
  dxl_wb.getPresentPositionData(motor[9], &presentposition[9], &log);
  dxl_wb.getPresentPositionData(motor[10], &presentposition[10], &log);
  dxl_wb.getPresentPositionData(motor[11], &presentposition[11], &log);
  dxl_wb.getPresentPositionData(motor[12], &presentposition[12], &log);


  if (initial_5 == 0) {
    initial_pos[5] = presentposition[5];
    initial_5++;
  }

  if (initial_6 == 0) {
    initial_pos[6] = presentposition[6];
    initial_6++;
  }

  if (initial_7 == 0) {
    initial_pos[7] = presentposition[7];
    initial_7++;
  }

  if (initial_8 == 0) {
    initial_pos[8] = presentposition[8];
    initial_8++;
  }

  if (initial_9 == 0) {
    initial_pos[9] = presentposition[9];
    initial_9++;
  }

   if (initial_10 == 0) {
    initial_pos[10] = presentposition[10];
    initial_10++;
  }

   if (initial_11 == 0) {
    initial_pos[11] = presentposition[11];
    initial_11++;
  }
     if (initial_12 == 0) {
    initial_pos[12] = presentposition[12];
    initial_12++;
  }




  //while (Serial.available()) {
  while (Serial2.available()) {

    String data = Serial2.readStringUntil(' ');
    if (data == "book5") {
      sensor_on[0] = 1;
      //distance[0] = Distance_sensing(0);
      dxl_wb.goalPosition(motor[5], (int32_t)(initial_pos[5] + 7900));
      motor_open[0] = 1;

    }
    if (data == "book6") {
      sensor_on[1] = 1;
      dxl_wb.goalPosition(motor[6], (int32_t)(initial_pos[6] + 7900));
      motor_open[1] = 1;
    }
    if (data == "book7") {
      sensor_on[2] = 1;
      dxl_wb.goalPosition(motor[7], (int32_t)(initial_pos[7] + 7900));
      motor_open[2] = 1;
    }
    if (data == "book8") {
      sensor_on[3] = 1;
      dxl_wb.goalPosition(motor[8], (int32_t)(initial_pos[8] + 7900));
      motor_open[3] = 1;
    }
    if (data == "book9") {
      sensor_on[4] = 1;
      dxl_wb.goalPosition(motor[9], (int32_t)(initial_pos[9] + 7900));
      motor_open[4] = 1;
    }
    if (data == "book10") { // 모터 거꾸로 달려있음 
      sensor_on[5] = 1;
      dxl_wb.goalPosition(motor[10], (int32_t)(initial_pos[10] -7900));
      motor_open[5] = 1;
    }
    if (data == "book11") {
      sensor_on[6] = 1;
      dxl_wb.goalPosition(motor[11], (int32_t)(initial_pos[11] + 7900));
      motor_open[6] = 1;
    }
    if (data == "book12") { // 모터 거꾸로 달려있음 
      sensor_on[7] = 1;
      dxl_wb.goalPosition(motor[12], (int32_t)(initial_pos[12] -7900));
      motor_open[7] = 1;
      
    }

    if (data == "reset5") {
      dxl_wb.goalPosition(motor[5], (int32_t)(initial_pos[5] + 100));
      motor_open[0] = 0;
      stack[0] = 0;
      sensor_on[0] = 0;
    }

    if (data == "reset6") {
      dxl_wb.goalPosition(motor[6], (int32_t)(initial_pos[6] + 100));
      motor_open[1] = 0;
      stack[1] = 0;
      sensor_on[1] = 0;
    }

    if (data == "reset7") {
      dxl_wb.goalPosition(motor[7], (int32_t)(initial_pos[7] + 100));
      motor_open[2] = 0;
      stack[2] = 0;
      sensor_on[2] = 0;
    }

    if (data == "reset8") {
      dxl_wb.goalPosition(motor[8], (int32_t)(initial_pos[8] + 100));
      motor_open[3] = 0;
      stack[3] = 0;
      //sensor_on[3] = 0; 초음파 센서 탑재 후 작성
    }

    if (data == "reset9") {
      dxl_wb.goalPosition(motor[9], (int32_t)(initial_pos[9] + 100));
      motor_open[4] = 0;
      stack[4] = 0;
      //sensor_on[4] = 0;
    }

    if (data == "reset10") { // 모터 거꾸로 달려있음 
      sensor_on[5] = 0;
      dxl_wb.goalPosition(motor[10], (int32_t)(initial_pos[10] -100));
      motor_open[5] = 0;

      //sensor_on[5] = 0;
    }

    if (data == "reset11") {
      dxl_wb.goalPosition(motor[11], (int32_t)(initial_pos[11] + 100));
      motor_open[6] = 0;
      stack[6] = 0;
      //sensor_on[6] = 0;
    }


    if (data == "reset12") { // 모터 거꾸로 달려있음 
      sensor_on[7] = 0;
      dxl_wb.goalPosition(motor[12], (int32_t)(initial_pos[12] -100));
      motor_open[7] = 0;

      //sensor_on[7] = 0;
    }


  }


  for (int i = 0 ; i < 5 ; i++) {

    if (sensor_on[i] == 1) {
      distance[i] = Distance_sensing(i);
    }

  }

  for (int i = 0 ; i < 5 ; i++) {

    if (distance[i] >= 60 && distance[i] <= 1000 && motor_open[i] == 1) {
      stack[i]++;
    }

  }


  //  for (int i = 0 ; i < 5 ; i++) {
  //
  //    if (stack[i] >= 5) {
  //      dxl_wb.goalPosition(motor[i + 5], (int32_t)(initial_pos[i + 5] + 100));
  //      motor_open[i] = 0;
  //      stack[i] = 0;
  //      sensor_on[i] = 0;
  //      str_msg2.data = shelf5;
  //    }
  //
  //  }

    if (stack[0] >= 3) {
    dxl_wb.goalPosition(motor[5], (int32_t)(initial_pos[5] + 100));
    motor_open[0] = 0;
    stack[0] = 0;
    sensor_on[0] = 0;
    }

    if (stack[1] >= 3) {
    dxl_wb.goalPosition(motor[6], (int32_t)(initial_pos[6] + 100));
    motor_open[1] = 0;
    stack[1] = 0;
    sensor_on[1] = 0;
    }

    if (stack[2] >= 3) {
    dxl_wb.goalPosition(motor[7], (int32_t)(initial_pos[7] + 100));
    motor_open[2] = 0;
    stack[2] = 0;
    sensor_on[2] = 0;
    }

    if (stack[3] >= 3) {
    dxl_wb.goalPosition(motor[8], (int32_t)(initial_pos[8] + 100));
    motor_open[3] = 0;
    stack[3] = 0;
    sensor_on[3] = 0;
    }

    if (stack[4] >= 3) {
    dxl_wb.goalPosition(motor[9], (int32_t)(initial_pos[9] + 100));
    motor_open[4] = 0;
    stack[4] = 0;
    sensor_on[4] = 0;
    }
    //일정 스택 이상 쌓이면 책장 서랍 자동으로 닫히게. 

    
  //  Serial.print("distance5: ");
  //  Serial.print(distance[0]);
  //  Serial.print("  ");
  //  Serial.print("distance6: ");
  //  Serial.print(distance[1]);
  //  Serial.print("  ");
  //  Serial.print("distance7: ");
  //  Serial.print(distance[2]);
  //  Serial.print("  ");
  //  Serial.print("distance8: ");
  //  Serial.print(distance[3]);
  //  Serial.print("  ");
  //  Serial.print("distance9: ");
  //  Serial.print(distance[4]);
  //  Serial.println("  \n");

}
