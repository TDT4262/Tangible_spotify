#include "HallSensor.h"

HallSensor Hall1(34);
HallSensor Hall2(35);
HallSensor Hall3(36);
HallSensor Hall4(37);
HallSensor Hall5(38);
HallSensor Hall6(39);
HallSensor Hall7(40);
HallSensor Hall8(41);
HallSensor Hall9(42);
HallSensor Hall10(43);
HallSensor Hall11(44);
HallSensor Hall12(45);
HallSensor Hall13(46);
HallSensor Hall14(47);
HallSensor Hall15(48);
HallSensor Hall16(49);
HallSensor Hall17(50);
HallSensor Hall18(51);
HallSensor Hall19(52);
//HallSensor Hall20(53);


void setup() { 
  Serial.begin(9600);       
}

void loop() {
  
if (Hall1.MagnetIsHere() == true)
  {
  Serial.println(Hall1.Letter());
  }
if (Hall2.MagnetIsHere() == true)
  {
  Serial.println(Hall2.Letter());
  }
if (Hall3.MagnetIsHere() == true)
  {
  Serial.println(Hall3.Letter());
  }
if (Hall4.MagnetIsHere() == true)
  {
  Serial.println(Hall4.Letter());
  }
if (Hall5.MagnetIsHere() == true)
  {
  Serial.println(Hall5.Letter());
  }
if (Hall6.MagnetIsHere() == true)
  {
  Serial.println(Hall6.Letter());
  }
if (Hall7.MagnetIsHere() == true)
  {
  Serial.println(Hall7.Letter());
  }
if (Hall8.MagnetIsHere() == true)
  {
  Serial.println(Hall8.Letter());
  }
if (Hall9.MagnetIsHere() == true)
  {
  Serial.println(Hall9.Letter());
  }
if (Hall10.MagnetIsHere() == true)
  {
  Serial.println(Hall10.Letter());
  }
if (Hall11.MagnetIsHere() == true)
  {
  Serial.println(Hall11.Letter());
  }
if (Hall12.MagnetIsHere() == true)
  {
  Serial.println(Hall12.Letter());
  }
if (Hall13.MagnetIsHere() == true)
  {
  Serial.println(Hall13.Letter());
  }
if (Hall14.MagnetIsHere() == true)
  {
  Serial.println(Hall14.Letter());
  }
if (Hall15.MagnetIsHere() == true)
  {
  Serial.println(Hall15.Letter());
  }
if (Hall16.MagnetIsHere() == true)
  {
  Serial.println(Hall16.Letter());
  }
if (Hall17.MagnetIsHere() == true)
  {
  Serial.println(Hall17.Letter());
  }
if (Hall18.MagnetIsHere() == true)
  {
  Serial.println(Hall18.Letter());
  }
if (Hall19.MagnetIsHere() == true)
  {
  Serial.println(Hall19.Letter());
  }
/*if (Hall20.MagnetIsHere() == true)
  {
  Serial.println(Hall20.Letter());
  }*/

else {
  Serial.println("null");
  }

delay(200);
}

