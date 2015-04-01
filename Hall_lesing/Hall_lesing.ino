#include "HalleffectSensor.h"

const int hallPin1 = 2; 
const int hallPin2 = 3;
const int hallPin3 = 4;
const int hallPin4 = 5;
const int hallPin5 = 6;
const int hallPin6 = 7; 
const int hallPin7 = 8;
const int hallPin8 = 9;
const int hallPin9 = 10;
const int hallPin10 = 11;


/*int hallState1 = 0;
int hallState2 = 0;
int hallState3 = 0;
int hallState4 = 0;
int hallState5 = 0;
int hallState6 = 0;
int hallState7 = 0;
int hallState8 = 0;
int hallState9 = 0;
int hallState10 = 0;*/

 

void setup() {
  
  Serial.begin(9600); 
  
  pinMode(hallPin1, INPUT); 
  pinMode(hallPin2, INPUT); 
  pinMode(hallPin3, INPUT);
  pinMode(hallPin4, INPUT); 
  pinMode(hallPin5, INPUT);
  pinMode(hallPin6, INPUT); 
  pinMode(hallPin7, INPUT); 
  pinMode(hallPin8, INPUT);
  pinMode(hallPin9, INPUT); 
  pinMode(hallPin10, INPUT);
  
   
}

void loop(){
  hallState1 = digitalRead(hallPin1);
  hallState2 = digitalRead(hallPin2);
  hallState3 = digitalRead(hallPin3);
  hallState4 = digitalRead(hallPin4);
  hallState5 = digitalRead(hallPin5);
  hallState6 = digitalRead(hallPin6);
  hallState7 = digitalRead(hallPin7);
  hallState8 = digitalRead(hallPin8);
  hallState9 = digitalRead(hallPin9);
  hallState10 = digitalRead(hallPin10);


  Serial.print(hallState7);
  Serial.print(hallState2);
  Serial.print(hallState5);
  Serial.print(hallState1);
  Serial.print(hallState10);
  Serial.print(hallState8);
  Serial.print(hallState4);
  Serial.print(hallState3);
  Serial.print(hallState6);
  Serial.println(hallState9);

  delay(10);
}

