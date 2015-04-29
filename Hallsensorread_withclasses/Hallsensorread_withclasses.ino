#include "HallSensor.h"
#include <RGBTools.h>

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
HallSensor Hall20(53);

RGBTools rgb(3,4,5);
int fadeSteps = 20;
int fadeTime = 500;

void setup() { 
  Serial.begin(9600);       
}

void loop() {
  
if (Hall1.MagnetIsHere() == true)
  {
  Serial.println(Hall1.Letter());
  rgb.fadeTo(153,51,255,fadeSteps,fadeTime); //blålilla: EDM
  }
if (Hall2.MagnetIsHere() == true)
  {
  Serial.println(Hall2.Letter());
  rgb.fadeTo(255,255,102,fadeSteps,fadeTime); //f.gul: SINGER SONGWRITER
  }
if (Hall3.MagnetIsHere() == true)
  {
  Serial.println(Hall3.Letter());
  rgb.fadeTo(0,255,0,fadeSteps,fadeTime); //grønn: POP
  }
if (Hall4.MagnetIsHere() == true)
  {
  Serial.println(Hall4.Letter());
  rgb.fadeTo(102,102,255,fadeSteps,fadeTime); //f.blå: AMBIENT
  }
if (Hall5.MagnetIsHere() == true)
  {
  Serial.println(Hall5.Letter());
  rgb.fadeTo(0,0,255,fadeSteps,fadeTime); //blå: BLUES
  }
if (Hall6.MagnetIsHere() == true)
  {
  Serial.println(Hall6.Letter());
  rgb.fadeTo(102,255,102,fadeSteps,fadeTime); //f.grønn: CLASSICAL
  }
if (Hall7.MagnetIsHere() == true)
  {
  Serial.println(Hall7.Letter());
  rgb.fadeTo(215,83,35,fadeSteps,fadeTime); //rødoransje: FUNK
  }
if (Hall8.MagnetIsHere() == true)
  {
  Serial.println(Hall8.Letter());
  rgb.fadeTo(51,255,255,fadeSteps,fadeTime); //blågrønn: JAZZ
  }
if (Hall9.MagnetIsHere() == true)
  {
  Serial.println(Hall9.Letter());
  rgb.fadeTo(255,255,0,fadeSteps,fadeTime); //gul: REGGAE
  }
if (Hall10.MagnetIsHere() == true)
  {
  Serial.println(Hall10.Letter());
  rgb.fadeTo(255,255,255,fadeSteps,fadeTime); //hvit: TOP 50
  }
if (Hall11.MagnetIsHere() == true)
  {
  Serial.println(Hall11.Letter());
  rgb.fadeTo(255,0,0,fadeSteps,fadeTime); //rød: METALL
  }
if (Hall12.MagnetIsHere() == true)
  {
  Serial.println(Hall12.Letter());
  rgb.fadeTo(232,170,26,fadeSteps,fadeTime); //guloransje: RNB
  }
if (Hall13.MagnetIsHere() == true)
  {
  Serial.println(Hall13.Letter());
  rgb.fadeTo(255,128,0,fadeSteps,fadeTime); //oransje: HIP-HOP
  }
if (Hall14.MagnetIsHere() == true)
  {
  Serial.println(Hall14.Letter());
  rgb.fadeTo(255,178,102,fadeSteps,fadeTime); //f.oransje: SOUL
  }
if (Hall15.MagnetIsHere() == true)
  {
  Serial.println(Hall15.Letter());
  rgb.fadeTo(153,255,51,fadeSteps,fadeTime); //gulgrønn: WORLD
  }
if (Hall16.MagnetIsHere() == true)
  {
  Serial.println(Hall16.Letter());
  rgb.fadeTo(255,102,255,fadeSteps,fadeTime); //f.lilla: ELECTRONICA
  }
if (Hall17.MagnetIsHere() == true)
  {
  Serial.println(Hall17.Letter());
  rgb.fadeTo(255,0,255,fadeSteps,fadeTime); //lilla: DUBSTEP
  }
if (Hall18.MagnetIsHere() == true)
  {
  Serial.println(Hall18.Letter());
  rgb.fadeTo(255,51,153,fadeSteps,fadeTime); //fiolett: HARDROCK
  }
if (Hall19.MagnetIsHere() == true)
  {
  Serial.println(Hall19.Letter());
  rgb.fadeTo(255,102,102,fadeSteps,fadeTime); //f.rød: ROCK
  }
/*if (Hall20.MagnetIsHere() == true)
  {
  Serial.println(Hall20.Letter());
  //rgb.fadeTo(0,0,0,fadeSteps,fadeTime); //ingen lyd
  }*/

else {
  Serial.println("null");
  }

delay(200);
}

