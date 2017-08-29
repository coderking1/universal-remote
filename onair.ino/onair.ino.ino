#include "IRremote.h"
IRsend irsend;
void setup()
{


Serial.begin(9600);
}

int khz=38; //NB Change this default value as neccessary to the correct modulation frequency
// ON and 2O C° with 1 FAN heat
unsigned ON[] ={4400,4300,550,1600,550,500,600,1550,550,1600,550,500,550,550,550,1550,550,550,550,500,550,1600,550,500,600,500,550,1550,600,1550,600,500,550,1550,600,500,550,500,600,500,550,1600,550,1550,550,1600,550,1600,550,1550,600,1550,600,1550,550,1600,550,500,550,550,550,500,550,550,550,500,550,550,550,1550,550,550,550,500,550,1600,550,500,550,550,550,500,550,1600,550,500,600,1550,600,1550,550,500,600,1550,550,1600,550,1550,600};

void loop() {

irsend.sendRaw(ON, sizeof(ON)/sizeof(int), khz);
delay(5000);

}