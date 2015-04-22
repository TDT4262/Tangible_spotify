#include "Arduino.h"

//extern char LetterList[14];

class HallSensor {
  public:
    HallSensor(int pin);
    bool MagnetIsHere();
    char Letter();
   
    
  private:
    int _pin;
    int HallState;
    char letter;
     
  
};
