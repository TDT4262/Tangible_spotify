#include "Arduino.h"
#include "HallSensor.h"


HallSensor::HallSensor(int pin) {
  _pin = pin;
  pinMode(_pin, INPUT);  
}

bool HallSensor::MagnetIsHere() { 
   HallState = digitalRead(_pin); 
   if (HallState == LOW) {
       return true; }
   else {
     return false; }
}
 
char HallSensor::Letter() { 
   char LetterList[23] = "abcdefghijklmnopqrstuv";
   letter = LetterList[_pin - 34]; //minus 34 fordi Hall1 skal ha bokstaven a (indeks 0)
   return letter;
}
 
