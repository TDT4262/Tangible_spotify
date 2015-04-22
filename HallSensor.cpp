#include "Arduino.h"
#include "HallSensor.h"


HallSensor::HallSensor(int pin) {
  _pin = pin;
  pinMode(_pin, INPUT);
  HallState = digitalRead(_pin); 
}

bool HallSensor::MagnetIsHere() { 
   if (HallState == LOW) {
       return true; }
   else {
     return false; }
}
 
char HallSensor::Letter() { 
   char LetterList[14] = "abcdefghijklm";
   letter = LetterList[_pin - 1] ;
   return letter;
}
 
