"""
this script uses the pyserial library to communicate with the arduino and vjoy library to communicate with the vjoy software
it opens the port that is in variable 'com' (check port number in arduino IDE)

check vjoy.py to see how the functions are called

note: only use prints for debugging, and comment them later, it induces a lot of delay, and makes setButton trigger on and off
"""
import serial
from vjoy import *
vj.open()
#put the com port here
com = 'COM17'
ser = serial.Serial(com,9600,write_timeout=0)
x = ser.read()
scale = 125
print(x)
if x == b"A":
    ser.write(b"B")
    while(True):
        #this reads the three bytes that were sent, so they will be in the same order, add more of these lines to get the values sent
        #note that the values sent should be integers and limited to one byte (0<= x <=254)
        A0 = int(ser.readline().decode("utf-8"))
        A1 = int(ser.readline().decode("utf-8"))
        Button = int(ser.readline().decode("utf-8"))
        setJoy(A0,A1, scale)
        #setButton receives two arguments, first one is the button number, here we trigger first button on controller, and second can be anything
        if Button == 1:
            setButton(1,1)
        #send valid byte to receive next data
        ser.write(b"B")

