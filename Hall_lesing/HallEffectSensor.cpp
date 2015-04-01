
HallEffectSensor::HallEffectSensor(int pin) {
  _pin = pin;
  digitalRead(_pin, INPUT);
}

//Trenger arbeid. Mye arbeid
