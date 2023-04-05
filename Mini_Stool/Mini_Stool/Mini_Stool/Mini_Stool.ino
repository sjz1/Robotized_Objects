#include <Button.h>
#include <Servo.h>
#define servoPin1 2
#define servoPin2 4
int value1;
int value2;
int value3;
Button mybutton(6);

Servo servo1;
Servo servo2;


void go(){
  
value1 = 130;
value2 = 60;
servo1.write(value1);
servo2.write(value1);
}

void sstop(){

value3 = 90;
servo1.write(value3);
servo2.write(value3);

}

void setup() {
Serial.begin(9600);
servo1.attach(servoPin1);
}

void loop() {
  mybutton.listen();
if (mybutton.onPress()) {
    go();
    delay(1500);
    sstop();  
}
}
