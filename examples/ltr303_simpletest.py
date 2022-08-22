# SPDX-FileCopyrightText: Copyright (c) 2022 ladyada for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense

import time
import board
from adafruit_ltr329_ltr303 import LTR303


i2c = board.I2C()  # uses board.SCL and board.SDA
from adafruit_debug_i2c import DebugI2C
debug_i2c = DebugI2C(i2c)

time.sleep(0.1) # sensor takes 100ms to 'boot' on power up
ltr303 = LTR303(debug_i2c)

ltr303.enable_int = True

while True:
    ltr303.int_polarity = not ltr303.int_polarity
    #print("Visible + IR:", ltr303.visible_plus_ir_light)
    #print("Infrared    :", ltr303.ir_light)
    #print("Visible     :", ltr303.visible_light)
    #print()
    time.sleep(0.5)  # sleep for half a second
