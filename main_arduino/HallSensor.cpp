#include "Arduino.h"
#include "HallSensor.h"


HallSensor::HallSensor(int pin) {
  _pin = pin;
  pinMode(_pin, INPUT);  
}

bool HallSensor::MagnetIsHere() { //Funksjon som returnerer true når sensoren trigges
   HallState = digitalRead(_pin); 
   if (HallState == LOW) {
       return true; }
   else {
     return false; }
}
 
char HallSensor::Letter() { //Funksjon som gir hver sensor en egen bokstav avhengig av hvilken pin de er koblet til
   char LetterList[23] = "abcdefghijklmnopqrstuv";
   letter = LetterList[_pin - 34]; //Minus 34 fordi det er laveste pin. Hallsensor 1 skal ha bokstaven a (indeks 0)
   return letter;
}
 
