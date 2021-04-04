/*
* Arduino Wireless Communication Tutorial
*       Example 1 - Receiver Code
*                
* by Dejan Nedelkovski, www.HowToMechatronics.com
* 
* Library: TMRh20/RF24, https://github.com/tmrh20/RF24/
*/

#include "printf.h"
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 radio(9, 10); // CE, CSN

#include "FastLED.h"

#define LED_PIN 3
#define LED_TYPE WS2812B
#define CHIPSET WS2812B
#define COLOR_ORDER GRB
#define NUM_LEDS 10
#define BRIGHTNESS 96

CRGB leds[NUM_LEDS];

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
  // Serial debugging
  Serial.begin(9600);
  
  radio.begin();
  radio.setChannel(channel);
  radio.setRetries(5, 15);
  radio.openReadingPipe(1, pipe);
  radio.setPALevel(RF24_PA_MIN);
  radio.setDataRate(RF24_1MBPS); 
  radio.setPayloadSize(sizeof(pixels));
  radio.startListening();
  
  printf_begin();             // needed only once for printing details
  radio.printDetails();       // (smaller) function that prints raw register values
  radio.printPrettyDetails(); // (larger) function that prints human readable data
   
  delay(1000);
  FastLED.addLeds<CHIPSET, LED_PIN, COLOR_ORDER>(leds, NUM_LEDS).setCorrection(TypicalLEDStrip);
  FastLED.setBrightness(BRIGHTNESS);
  
  fill_solid(leds, NUM_LEDS, CRGB(10, 10, 10));
  FastLED.show();
}

unsigned int wait = 0;
bool sleep = false;

void loop() {
  radio.startListening();
  uint8_t pipe;
  if (radio.available(&pipe)) {
    Serial.println("radio.available()");
    wait = 0;
    sleep = false;
    radio.read(&pixels, sizeof(pixels));
    for (unsigned int i = 0; i < NUM_LEDS; i++) {
      leds[i].setRGB(pixels[i].r, pixels[i].g, pixels[i].b);
    }
    FastLED.show();
//    FastLED.delay(8);
    return;
  }
  
  if (sleep) {
    Serial.println("sleep");
//    radio.stopListening();
    delay(1000);
    return;
  }
  
  wait++;
  if (wait > 30000) {
    Serial.println("wait 30000 exceeded. sleeping.");
    FastLED.clear();
    FastLED.show(); 
    sleep = true;
  }
}
