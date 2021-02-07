// (c) Michael Schoeffler 2017, http://www.mschoeffler.de
#include "FastLED.h"

#define LED_PIN 3
#define LED_TYPE WS2812B
#define CHIPSET WS2812B
#define COLOR_ORDER GRB
#define NUM_LEDS 10
#define BRIGHTNESS 96

CRGB leds[NUM_LEDS];

void loop()
{
  static uint8_t starthue = 0;
  fill_rainbow(leds, NUM_LEDS, --starthue, 20);

  FastLED.show();
  FastLED.delay(8);
}

void setup() {
  delay(3000);
  FastLED.addLeds<CHIPSET, LED_PIN, COLOR_ORDER>(leds, NUM_LEDS).setCorrection(TypicalLEDStrip);
  FastLED.setBrightness(BRIGHTNESS);
}
