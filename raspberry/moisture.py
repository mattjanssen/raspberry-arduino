import sys
import argparse
import time
import struct
from dataclasses import dataclass
import RPi.GPIO as GPIO
from RF24 import *

# 0 - 124
channel = 117

pipeNum = 1
writePipe = 0x58857576500
# readPipe = 0x0000000001

radio = RF24(22, 0)

@dataclass
class SensorData:
    counter: int
    def __bytes__(self):
        return bytes([self.counter])

payload = SensorData(0)

def loop():
    while True:
        time.sleep(2)
        payload.counter = payload.counter + 1
        if payload.counter == 256:
            payload.counter = 0
        print("Write: " + str(payload.counter))
        result = radio.write(bytes(payload))
        if not result:
            print("Write 1 failed.")
            break
        
        radio.startListening()
        while True:
            if not radio.available():
                # @TODO Limit waiting time.
                continue
            response = radio.read(len(bytes(payload)))
            # print("Read: " + str(response[0]))
            radio.stopListening()  # put radio in TX mode
            break

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
    # RF24_PA_MIN RF24_PA_LOW RF24_PA_HIGH RF24_PA_MAX
    radio.setPALevel(RF24_PA_MIN)

    # ?
    # RF24_250KBPS RF24_1MBPS RF24_2MBPS
    radio.setDataRate(RF24_250KBPS); 

    # Maybe?
    radio.setChannel(channel)

    # set the TX address of the RX node into the TX pipe
    radio.openWritingPipe(writePipe)
    radio.openReadingPipe(pipeNum, writePipe)

    # set the RX address of the TX node into a RX pipe
    # radio.openReadingPipe(1, address[not radio_number])  # using pipe 1
    # radio.openReadingPipe(1, readPipe)  # using pipe 1

    # To save time during transmission, we'll set the payload size to be only
    # what we need. A float value occupies 4 bytes in memory using
    # struct.pack(); "<f" means a little endian unsigned float
    radio.payloadSize = len(bytes(payload))
    # radio.enableDynamicPayloads()

    # From tutorial.
    # radio.enableDynamicPayloads()
    radio.setRetries(15, 15)
    # radio.setRetries(5, 15)

    # radio.setAutoAck(True)
    # radio.enableAckPayload()

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
