/*
* Arduino Wireless Communication Tutorial
*     Example 1 - Transmitter Code
*                
* by Dejan Nedelkovski, www.HowToMechatronics.com
* 
* Library: TMRh20/RF24, https://github.com/tmrh20/RF24/
*/

#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

#define NUM_LEDS 10

RF24 radio(9, 10); // CE, CSN

// 0 - 124
const byte channel = 42;

const uint64_t pipe = 0xB3F5B5DA00LL;

struct RGBData {
  byte r;
  byte g;
  byte b;
};

RGBData pixels[NUM_LEDS];

void setup() {
//  Serial.begin(9600);
  
  radio.begin();
  radio.setChannel(channel);
  radio.setRetries(5, 15);
  radio.openWritingPipe(pipe);
  radio.setPALevel(RF24_PA_MIN);
  radio.setDataRate(RF24_1MBPS); 
  radio.setPayloadSize(sizeof(pixels));
  radio.stopListening();
}

const int speed = 20;

void loop() {
  setColor(255, 0, 0);    // red
  setColor(0, 255, 0);    // green
  setColor(0, 0, 255);    // blue
}

byte r = 0;
byte g = 0;
byte b = 0;

void setColor(byte red, byte green, byte blue) {
  while ( r != red || g != green || b != blue ) {
    if ( r < red ) r = min(r + speed, red);
    if ( r > red ) r = max(r - speed, red);

    if ( g < green ) g = min(g + speed, green);
    if ( g > green ) g = max(g - speed, green);

    if ( b < blue ) b = min(b + speed, blue);
    if ( b > blue ) b = max(b - speed, blue);

    _setColor();
//    delay(10);
  }
}

void _setColor() {
  for (unsigned int p = NUM_LEDS - 1; p > 0; p--) {
    pixels[p] = pixels[p - 1];
  }
  pixels[0] = {r, g, b};
  
  radio.write(&pixels, sizeof(pixels));
}
