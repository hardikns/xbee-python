#! /usr/bin/python

# Import and init an XBee device
from xbee import XBee
import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600)

# Use an XBee 802.15.4 device
# To use with an XBee ZigBee device, replace with:
#xbee = ZigBee(ser)
xbee = XBee(ser)


device={
        "CO3":'\x00\x13\xa2\x00\x40\x52\x8d\x8a',
        "EP1":'\x00\x13\xa2\x00\x40\xb5\xb1\x0b'
}


led=False

#change remote device function
xbee.remote_at(dest_addr_long=device["EP1"],command='D2',parameter='\x02')
xbee.remote_at(dest_addr_long=device["EP1"],command='D1',parameter='\x03')
xbee.remote_at(dest_addr_long=device["EP1"],command='IR',parameter='\x04\x00')
xbee.remote_at(dest_addr_long=device["EP1"],command='IC',parameter='\x02')

while 1:
        #set led status
        led=not led
        if led:
                print "switching Off Light"
                xbee.remote_at(dest_addr_long=device["EP1"],command='D0',parameter='\x04')
        else:
                print "switching on Light"
                xbee.remote_at(dest_addr_long=device["EP1"],command='D0',parameter='\x05')
        # wait 1 second
        time.sleep(5)
        
ser.close()


