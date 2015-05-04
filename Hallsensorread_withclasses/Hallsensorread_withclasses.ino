#include "HallSensor.h" //Klasse for behandling av Hall Sensor input
#include <RGBTools.h> //Et bibliotek vi har brukt for å styre LED-lyset

/*Oppretter objekter for alle sensorene.
Hver av disse objektene vil sende en egen bokstav til SerialPort når
sensorene de er knyttet til registrerer et magnetfelt.*/

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

RGBTools rgb(11,12,13);
int fadeSteps = 20;
int fadeTime = 500;

const int button = 2; //Knapp for å stjernemarkere sanger


void setup() { 
  Serial.begin(9600);   
  pinMode(button, INPUT);
}

void loop() {
 //Lang if-setning som sjekker alle sensor-input og sender bokstaver til SerialPort
  
if (Hall1.MagnetIsHere() == true)
  {
  Serial.println(Hall1.Letter());
  rgb.fadeTo(70,204,0,fadeSteps,fadeTime); //A blålilla: EDM
  }
if (Hall2.MagnetIsHere() == true)
  {
  Serial.println(Hall2.Letter());
  rgb.fadeTo(0,53,200,fadeSteps,fadeTime); //B f.gul: SINGER SONGWRITER
  }
if (Hall3.MagnetIsHere() == true)
  {
  Serial.println(Hall3.Letter());
  rgb.fadeTo(255,0,255,fadeSteps,fadeTime); //C grønn: BIG BAND
  }
if (Hall4.MagnetIsHere() == true)
  {
  Serial.println(Hall4.Letter());
  rgb.fadeTo(153,153,0,fadeSteps,fadeTime); //D f.blå: AMBIENT
  }
if (Hall5.MagnetIsHere() == true)
  {
  Serial.println(Hall5.Letter());
  rgb.fadeTo(255,255,0,fadeSteps,fadeTime); //E blå: BLUES
  }
if (Hall6.MagnetIsHere() == true)
  {
  Serial.println(Hall6.Letter());
  rgb.fadeTo(153,0,153,fadeSteps,fadeTime); //F f.grønn: CLASSICAL
  }
if (Hall7.MagnetIsHere() == true)
  {
  Serial.println(Hall7.Letter());
  rgb.fadeTo(0,235,255,fadeSteps,fadeTime); //G rødoransje: FUNK
  }
if (Hall8.MagnetIsHere() == true)
  {
  Serial.println(Hall8.Letter());
  rgb.fadeTo(204,0,0,fadeSteps,fadeTime); //H blågrønn: JAZZ
  }
if (Hall9.MagnetIsHere() == true)
  {
  Serial.println(Hall9.Letter());
  rgb.fadeTo(0,153,255,fadeSteps,fadeTime); //I gul: REGGAE
  }
if (Hall10.MagnetIsHere() == true)
  {
  Serial.println(Hall10.Letter());
  rgb.fadeTo(0,77,153,fadeSteps,fadeTime); //J hvit: POP
  }
if (Hall11.MagnetIsHere() == true)
  {
  Serial.println(Hall11.Letter());
  rgb.fadeTo(0,255,255,fadeSteps,fadeTime); //K rød: METAL
  }
if (Hall12.MagnetIsHere() == true)
  {
  Serial.println(Hall12.Letter());
  rgb.fadeTo(0,200,255,fadeSteps,fadeTime); //L guloransje: R&B
  }
if (Hall13.MagnetIsHere() == true)
  {
  Serial.println(Hall13.Letter());
  rgb.fadeTo(0,220,255,fadeSteps,fadeTime); //M oransje: HIP-HOP
  }
if (Hall14.MagnetIsHere() == true)
  {
  Serial.println(Hall14.Letter());
  rgb.fadeTo(30,200,255,fadeSteps,fadeTime); //N f.oransje: SOUL
  }
if (Hall15.MagnetIsHere() == true)
  {
  Serial.println(Hall15.Letter());
  rgb.fadeTo(0,102,255,fadeSteps,fadeTime); //O gulgrønn: WORLD
  }
if (Hall16.MagnetIsHere() == true)
  {
  Serial.println(Hall16.Letter());
  rgb.fadeTo(0,153,0,fadeSteps,fadeTime); //P f.lilla: ELECTRONICA
  }
if (Hall17.MagnetIsHere() == true)
  {
  Serial.println(Hall17.Letter());
  rgb.fadeTo(0,204,0,fadeSteps,fadeTime); //Q lilla: DUBSTEP
  }
if (Hall18.MagnetIsHere() == true)
  {
  Serial.println(Hall18.Letter());
  rgb.fadeTo(0,204,153,fadeSteps,fadeTime); //R fiolett: HARDROCK
  }
if (Hall19.MagnetIsHere() == true)
  {
  Serial.println(Hall19.Letter());
  rgb.fadeTo(0,225,240,fadeSteps,fadeTime); //S f.rød: ROCK
  }
if (Hall20.MagnetIsHere() == true)
  {
  Serial.println(Hall20.Letter());
  rgb.fadeTo(255,255,255,fadeSteps,fadeTime); //T ingen lys: ingen lyd
  }
if(digitalRead(button)==HIGH)
  {
  Serial.println('u'); //U knapp: stjernemarkering av sang
  }
else {
  Serial.println("null"); //Printer 'null' om ingenting ovenfor trigges
  }

delay(200);
}

