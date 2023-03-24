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
#define MOTOR13 13
#define MOTOR14 14
#define MOTOR15 15
#define MOTOR16  16
#define MOTOR17  17
#define MOTOR18  18
#define MOTOR19  19
#define MOTOR20  20
#define MOTOR21  21
#define MOTOR22  22
#define MOTOR23  23
#define MOTOR24  24
#define MOTOR25 25
#define MOTOR26 26
#define MOTOR27 27
#define MOTOR28 28
#define MOTOR29 29
#define MOTOR30 30



DynamixelWorkbench dxl_wb;

int motor_open[30] = {0,};
int sensor_on[30] = {0,};
int stack[30] = {0,};

uint16_t model_number = 0;
int32_t presentposition[30];
uint8_t motor[30] = {0, MOTOR1, MOTOR2, MOTOR3, MOTOR4, MOTOR5, MOTOR6, MOTOR7, MOTOR8, MOTOR9, MOTOR10, MOTOR11, MOTOR12, MOTOR13, MOTOR14, MOTOR15, MOTOR16, MOTOR17, MOTOR18, MOTOR19, MOTOR20, MOTOR21, MOTOR22, MOTOR23, MOTOR24, MOTOR25, MOTOR26, MOTOR27, MOTOR28, MOTOR29};



void setup() {

  Serial.begin(9600);
  Serial2.begin(9600);
}

void loop() {

  const char *log;
  dxl_wb.init(DEVICE_NAME, BAUDRATE, &log);
  for (int i = 1; i <= 10; i++)
  {
    dxl_wb.ping(motor[i], &model_number, &log);
  }
  for (int j = 1; j <= 10; j++)
  {
    dxl_wb.setExtendedPositionControlMode(motor[j], &log);
  }

  for (int k = 1; k <= 10; k++)
  {
    dxl_wb.torqueOn(motor[k], &log);
  }

  for (int l = 1; l <= 10; l++)
  {
    dxl_wb.getPresentPositionData(motor[l], &presentposition[l], &log);
  }

    

  for (int m = 1; m <= 10; m++)
  {
    dxl_wb.goalPosition(motor[m], (int32_t)(presentposition[m] + 7900));
    delay(3000);
    dxl_wb.goalPosition(motor[m], (int32_t)(presentposition[m] + 100));
    delay(3000);
  }


  delay(100);
}
