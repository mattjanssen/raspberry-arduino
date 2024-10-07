from .fastled_config import *

# @file FastLED.h
# central include file for FastLED, defines the CFastLED class/object

FASTLED_VERSION = 3003002
#  ifndef FASTLED_INTERNAL
#    ifdef FASTLED_HAS_PRAGMA_MESSAGE
#      pragma message "FastLED version 3.003.003"
#    else
#      warning FastLED version 3.003.003  (Not really a warning, just telling you here.)
#    endif
#  endif


# ifdef SmartMatrix_h
# include <SmartMatrix.h>
# endif

# ifdef DmxSimple_h
# include <DmxSimple.h>
# endif

# ifdef DmxSerial_h
# include <DMXSerial.h>
# endif

import time

from .cpp_compat import *

from .fastled_config import *
from .fastled_config import __FASTLED_HAS_FIBCC
# from .led_sysdefs import *
\
# Utility functions
# from .fastled_delay import *
# from .bitswap import *

# from .controller import *
# from .fastpin import *
# from .fastspi_types import *
# from .dmx import *

# from .platforms import *
# from .fastled_progmem import *

from .lib8tion import *
from .pixeltypes import *
from .hsv2rgb import *
from .colorutils import *
from .pixelset import *
from .colorpalettes import *

from .noise import *
# from .power_mgt import *

# from .fastspi import *
# from .chipsets import *

# definitions for the spi chipset constants
LPD6803 = 0
LPD8806 = 1
WS2801 = 2
WS2803 = 3
SM16716 = 4
P9813 = 5
APA102 = 6
SK9822 = 7
DOTSTAR = 8

SMART_MATRIX = 0
OCTOWS2811 = 0
OCTOWS2811_400 = 1
OCTOWS2813 = 2
WS2812SERIAL = 0


# class PIXIE(PixieController):
#     def __init__(self, DATA_PIN, RGB_ORDER):
#         PixieController.__init__(self, DATA_PIN, RGB_ORDER)


# class NEOPIXEL(WS2812Controller800Khz):
#     def __init__(self, DATA_PIN, GRB):
#         WS2812Controller800Khz.__init__(self, DATA_PIN, GRB)


# class SM16703(SM16703Controller):
#     def __init__(self, DATA_PIN, RGB_ORDER):
#         SM16703Controller.__init__(self, DATA_PIN, RGB_ORDER)


# class TM1829(TM1829Controller800Khz):
#     def __init__(self, DATA_PIN, RGB_ORDER):
#         TM1829Controller800Khz.__init__(self, DATA_PIN, RGB_ORDER)


# class TM1812(TM1809Controller800Khz):
#     def __init__(self, DATA_PIN, RGB_ORDER):
#         TM1809Controller800Khz.__init__(self, DATA_PIN, RGB_ORDER)


# class TM1809(TM1809Controller800Khz):
#     def __init__(self, DATA_PIN, RGB_ORDER):
#         TM1809Controller800Khz.__init__(self, DATA_PIN, RGB_ORDER)


# class TM1804(TM1809Controller800Khz):
#     def __init__(self, DATA_PIN, RGB_ORDER):
#         TM1809Controller800Khz.__init__(self, DATA_PIN, RGB_ORDER)


# class TM1803(TM1803Controller400Khz):
#     def __init__(self, DATA_PIN, RGB_ORDER):
#         TM1803Controller400Khz.__init__(self, DATA_PIN, RGB_ORDER)


# class UCS1903(UCS1903Controller400Khz):
#     def __init__(self, DATA_PIN, RGB_ORDER):
#         UCS1903Controller400Khz.__init__(self, DATA_PIN, RGB_ORDER)


# class UCS1903B(UCS1903BController800Khz):
#     def __init__(self, DATA_PIN, RGB_ORDER):
#         UCS1903BController800Khz.__init__(self, DATA_PIN, RGB_ORDER)


# class UCS1904(UCS1904Controller800Khz):
#     def __init__(self, DATA_PIN, RGB_ORDER):
#         UCS1904Controller800Khz.__init__(self, DATA_PIN, RGB_ORDER)


# class UCS2903(UCS2903Controller):
#     def __init__(self, DATA_PIN, RGB_ORDER):
#         UCS2903Controller.__init__(self, DATA_PIN, RGB_ORDER)


# class WS2812(WS2812Controller800Khz):
#     def __init__(self, DATA_PIN, RGB_ORDER):
#         WS2812Controller800Khz.__init__(self, DATA_PIN, RGB_ORDER)


# class WS2852(WS2812Controller800Khz):
#     def __init__(self, DATA_PIN, RGB_ORDER):
#         WS2812Controller800Khz.__init__(self, DATA_PIN, RGB_ORDER)


# class WS2812B(WS2812Controller800Khz):
#     def __init__(self, DATA_PIN, RGB_ORDER):
#         WS2812Controller800Khz.__init__(self, DATA_PIN, RGB_ORDER)


# class GS1903(WS2812Controller800Khz):
#     def __init__(self, DATA_PIN, RGB_ORDER):
#         WS2812Controller800Khz.__init__(self, DATA_PIN, RGB_ORDER)


# class SK6812(SK6812Controller):
#     def __init__(self, DATA_PIN, RGB_ORDER):
#         SK6812Controller.__init__(self, DATA_PIN, RGB_ORDER)


# class SK6822(SK6822Controller):
#     def __init__(self, DATA_PIN, RGB_ORDER):
#         SK6822Controller.__init__(self, DATA_PIN, RGB_ORDER)


# class APA106(SK6822Controller):
#     def __init__(self, DATA_PIN, RGB_ORDER):
#         SK6822Controller.__init__(self, DATA_PIN, RGB_ORDER)


# class PL9823(PL9823Controller):
#     def __init__(self, DATA_PIN, RGB_ORDER):
#         PL9823Controller.__init__(self, DATA_PIN, RGB_ORDER)


# class WS2811(WS2811Controller800Khz):
#     def __init__(self, DATA_PIN, RGB_ORDER):
#         WS2811Controller800Khz.__init__(self, DATA_PIN, RGB_ORDER)


# class WS2813(WS2813Controller):
#     def __init__(self, DATA_PIN, RGB_ORDER):
#         WS2813Controller.__init__(self, DATA_PIN, RGB_ORDER)


# class APA104(WS2811Controller800Khz):
#     def __init__(self, DATA_PIN, RGB_ORDER):
#         WS2811Controller800Khz.__init__(self, DATA_PIN, RGB_ORDER)


# class WS2811_400(WS2811Controller400Khz):
#     def __init__(self, DATA_PIN, RGB_ORDER):
#         WS2811Controller400Khz.__init__(self, DATA_PIN, RGB_ORDER)


# class GE8822(GE8822Controller800Khz):
#     def __init__(self, DATA_PIN, RGB_ORDER):
#         GE8822Controller800Khz.__init__(self, DATA_PIN, RGB_ORDER)


# class GW6205(GW6205Controller800Khz):
#     def __init__(self, DATA_PIN, RGB_ORDER):
#         GW6205Controller800Khz.__init__(self, DATA_PIN, RGB_ORDER)


# class GW6205_400(GW6205Controller400Khz):
#     def __init__(self, DATA_PIN, RGB_ORDER):
#         GW6205Controller400Khz.__init__(self, DATA_PIN, RGB_ORDER)


# class LPD1886(LPD1886Controller1250Khz):
#     def __init__(self, DATA_PIN, RGB_ORDER):
#         LPD1886Controller1250Khz.__init__(self, DATA_PIN, RGB_ORDER)


# class LPD1886_8BIT(LPD1886Controller1250Khz_8bit):
#     def __init__(self, DATA_PIN, RGB_ORDER):
#         LPD1886Controller1250Khz_8bit.__init__(self, DATA_PIN, RGB_ORDER)


# class DMXSIMPLE(DMXSimpleController):
#     def __init__(self, DATA_PIN, RGB_ORDER):
#         DMXSimpleController.__init__(self, DATA_PIN, RGB_ORDER)


# class DMXSERIAL(DMXSerialController):
#     def __init__(self, RGB_ORDER):
#         DMXSerialController.__init__(self, RGB_ORDER)


WS2811_PORTA = 0
WS2813_PORTA = 1
WS2811_400_PORTA = 2
TM1803_PORTA = 3
UCS1903_PORTA = 4

WS2811_PORTB = 0
WS2813_PORTB = 1
WS2811_400_PORTB = 2
TM1803_PORTB = 3
UCS1903_PORTB = 4

WS2811_PORTC = 0
WS2813_PORTC = 1
WS2811_400_PORTC = 2
TM1803_PORTC = 3
UCS1903_PORTC = 4

WS2811_PORTD = 0
WS2813_PORTD = 1
WS2811_400_PORTD = 2
TM1803_PORTD = 3
UCS1903_PORTD = 4

WS2811_PORTDC = 5
WS2813_PORTDC = 6
WS2811_400_PORTDC = 7
TM1803_PORTDC = 8
UCS1903_PORTDC = 9

NUM_CONTROLLERS = 8


fuckit = 0
pSmartMatrix = None

# CLEDController.m_pHead = None
# CLEDController.m_pTail = None
lastshow = 0

_frame_cnt = 0
_retry_cnt = 0
noise_min = 0
noise_max = 0


# uint32_t CRGB::Squant = ((uint32_t)((__TIME__[4]-'0') * 28))<<16 | ((__TIME__[6]-'0')*50)<<8 | ((__TIME__[7]-'0')*28)






