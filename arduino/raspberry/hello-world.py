import sys
import argparse
import time
import struct
from dataclasses import dataclass
import RPi.GPIO as GPIO
from RF24 import *

# struct RGBData {
#   byte r;
#   byte g;
#   byte b;
# };
# RGBData pixels[NUM_LEDS];

# 0 - 124
channel = 42

writePipe = 0xB3F5B5DA00
# readPipe = 0x0000000001

radio = RF24(22, 0)

@dataclass
class RGBData:
    r: int
    g: int
    b: int
    def __bytes__(self):
        return bytes([self.r, self.g, self.b])

NUM_LEDS = 10
SPEED = 20

pixels = [RGBData(0, 0, 0)] * NUM_LEDS

color = RGBData(0, 0, 0)

def loop():
    radio.stopListening()  # put radio in TX mode

    while True:
        setColor(255, 0, 0)
        setColor(0, 255, 0)
        setColor(0, 0, 255)

def setColor(red: int, green: int, blue: int):
    while color.r != red or color.g != green or color.b != blue:
        if (color.r < red):   color.r = min(color.r + SPEED, red)
        if (color.r > red):   color.r = max(color.r - SPEED, red)
        if (color.g < green): color.g = min(color.g + SPEED, green)
        if (color.g > green): color.g = max(color.g - SPEED, green)
        if (color.b < blue):  color.b = min(color.b + SPEED, blue)
        if (color.b > blue):  color.b = max(color.b - SPEED, blue)
        sendColors()

def sendColors():
    for p in reversed(range(1, NUM_LEDS)):
        pixels[p] = pixels[p - 1]

    pixels[0] = RGBData(color.r, color.g, color.b)
  
    buffer = bytearray(b''.join([bytes(x) for x in pixels]))
    result = radio.write(buffer)

def send():
    """Transmits an incrementing float every second"""
    failures = 0
    while failures < 6:
        # use struct.pack() to packet your data into the payload
        # "<f" means a single little endian (4 byte) float value.
        # buffer = struct.pack("<f", payload[0])
        buffer = bytearray(b''.join([bytes(x) for x in pixels]))
        start_timer = time.monotonic_ns()  # start timer
        result = radio.write(buffer)
        end_timer = time.monotonic_ns()  # end timer
        pixels[0].r += 16
        print("Sent {} bytes".format(len(buffer)))
        if not result:
            print("Transmission failed or timed out")
            failures += 1
        else:
            print(
                "Transmission successful! Time to Transmit: "
                "{} us. Sent: {}".format(
                    (end_timer - start_timer) / 1000,
                    pixels
                )
            )
        # time.sleep(1)
    print(failures, "failures detected. Leaving TX role.")

if __name__ == "__main__":
    # initialize the nRF24L01 on the spi bus
    if not radio.begin():
        raise RuntimeError("radio hardware is not responding")

    # For this example, we will use different addresses
    # An address need to be a buffer protocol object (bytearray)
    # address = [b"1Node", b"2Node"]

    # It is very helpful to think of an address as a path instead of as
    # an identifying device destination

    print(sys.argv[0])  # print example name

    # set the Power Amplifier level to -12 dBm since this test example is
    # usually run with nRF24L01 transceivers in close proximity of each other
    radio.setPALevel(RF24_PA_MIN)  # RF24_PA_MAX is default

    # ?
    radio.setDataRate(RF24_1MBPS); 

    # Maybe?
    radio.setChannel(channel)

    # set the TX address of the RX node into the TX pipe
    radio.openWritingPipe(writePipe)

    # set the RX address of the TX node into a RX pipe
    # radio.openReadingPipe(1, address[not radio_number])  # using pipe 1
    # radio.openReadingPipe(1, readPipe)  # using pipe 1

    # To save time during transmission, we'll set the payload size to be only
    # what we need. A float value occupies 4 bytes in memory using
    # struct.pack(); "<f" means a little endian unsigned float
    # radio.payloadSize = len(struct.pack("<f", payload[0]))
    radio.payloadSize = len(b''.join([bytes(x) for x in pixels]))

    # From tutorial.
    # radio.enableDynamicPayloads()
    radio.setRetries(5, 15)

    # for debugging, we have 2 options that print a large block of details
    # (smaller) function that prints raw register values
    radio.printDetails()
    # (larger) function that prints human readable data
    radio.printPrettyDetails()

    try:
        loop()
    except KeyboardInterrupt:
        print(" Keyboard Interrupt detected. Exiting...")
        radio.powerDown()
        sys.exit()
