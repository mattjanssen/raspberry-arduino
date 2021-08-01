
#include "printf.h"
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 radio(9, 10); // CE, CSN

// 0 - 124
const byte channel = 117;

const uint64_t pipe = 0x58857576500;

const uint8_t pipeNum = 1;

struct PayloadStruct {
  uint8_t counter;
};
PayloadStruct payload = { counter: 123 };

void setup() {
//  Serial.begin(9600);
  analogReference(EXTERNAL); // set the analog reference to 3.3V
  
  radio.begin();
  radio.setChannel(channel);
  radio.setRetries(15, 15);
  radio.openWritingPipe(pipe);
  radio.openReadingPipe(pipeNum, pipe);
  radio.setPALevel(RF24_PA_MIN); // RF24_PA_MIN RF24_PA_LOW RF24_PA_HIGH RF24_PA_MAX
  radio.setDataRate(RF24_250KBPS); // RF24_250KBPS RF24_1MBPS RF24_2MBPS
  radio.setPayloadSize(sizeof(payload));

//  radio.setAutoAck(true);
//  radio.enableDynamicPayloads();
//  radio.enableAckPayload();
  
  radio.startListening();
  
  printf_begin();             // needed only once for printing details
  radio.printDetails();       // (smaller) function that prints raw register values
  radio.printPrettyDetails(); // (larger) function that prints human readable data
}

int ackCounter = 0;

unsigned int wait = 0;
bool sleep = false;

void loop() {
//  Serial.print("#0: ");
//  Serial.print((float(analogRead(A0))/1023.0)*5.0); // read sensor
//  Serial.print(" V");
//  Serial.print(" #1: ");
//  Serial.print((float(analogRead(A1))/1023.0)*5.0); // read sensor
//  Serial.println(" V");
  
  uint8_t pipe;
  
  if (radio.available(&pipe)) {
    radio.read(&payload, sizeof(payload));
    Serial.print("Read complete: ");
    Serial.println(payload.counter);

//    int value = float(analogRead(A1))/1023.0*255;
    ackCounter++;
    payload.counter = ackCounter;
    Serial.print("Sending response: ");
    Serial.println(payload.counter);
    
    radio.stopListening();
    radio.write(&payload, sizeof(payload));
    radio.startListening();
    
    wait = 0;
    sleep = false;

    return;
  }
  
  if (sleep) {
    Serial.println("sleep");
    delay(1000);
    
    return;
  }
  
  wait++;
  if (wait > 30000) {
    Serial.println("wait exceeded. sleeping.");
    sleep = true;
  }
}
