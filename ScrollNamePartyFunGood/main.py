### Author: pixelpusher team
### Description: Scroll your name
### Category: Creative
### License: MIT
### Appname : ScrollNamePartyFunGood

import dialogs
from database import *
import buttons
import ugfx
from imu import IMU

ugfx.init()
buttons.init()
ugfx.init()

imu = IMU()

backgrounds = [ugfx.YELLOW, ugfx.GRAY, ugfx.RED, ugfx.BLUE, ugfx.GREEN, ugfx.ORANGE, ugfx.PURPLE]
ugfx.set_default_font(ugfx.FONT_NAME)
ugfx.area(0,0,ugfx.width(),ugfx.height(),0)
cx = int(ugfx.width() / 2);
cy = int(ugfx.height() / 2);
speed = 32 # scroll speed

with Database() as db:
    name = db.get("display-name", "Matt Daemon")
    position = 0
    colorIndex = 0
    name_len = len(name)*32

    while True:

        # set orientation
        flip = 1
        ival = imu.get_acceleration()
        if ival['y'] < 0:
        	ugfx.orientation(0)
        else:
        	ugfx.orientation(180)

        if ival['y'] < 0:
            flip = -1

        # estimate 10 characters per screen...
        ugfx.clear(backgrounds[colorIndex])
        colorIndex += 1
        colorIndex %= len(backgrounds)
        accel = ival['x']*flip # -1 to 1

        # Center middle
        # estimate 32px per character... ugly
        position += int(accel*speed)
        if (position > name_len):
            position = -name_len
        if (position < -name_len):
            position = name_len

        ugfx.text(position-name_len, cy, name, ugfx.BLACK)
        ugfx.text(position, cy, name, ugfx.WHITE)
        ugfx.text(position+name_len, cy, name, ugfx.BLACK)

        pyb.delay(100)
