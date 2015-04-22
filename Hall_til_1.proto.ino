#include "HallSensor.h"

HallSensor Hall2(2);

void setup() {
  
  Serial.begin(9600);       
}

void loop(){

if (Hall2.MagnetIsHere() == true)
  {
  Serial.println(Hall2.Letter());
  }
else {
  Serial.println("nei");
  }

delay(100);
}

