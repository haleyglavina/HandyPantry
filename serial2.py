import serial
from time import sleep
port = "/dev/ttyACM0" # Port that Arduino plugs into on Pi
# If port not found, type into terminal: ls /dev/tty* and choose ACM_ that appears
baudrate = 9600
ser = serial.Serial(port, baudrate)

# Sends integer from RPi to Arduino
def tellNum(num):
    num_encode = b'%d' %num
    ser.write(num_encode)

# Receives number from Arduino and returns it
def hear():
    while not(ser.in_waiting>0): # If we have stuff in input buffer
        continue
    msg = bytearray()
    if (ser.in_waiting>0):
        msg += ser.readline() # read until a new line
        mystring = msg.decode('utf-8')  # decode as utf-8 removes b in front of value
    mystring = mystring[:-1] # Remove non-numeric character from end of the input stream
    myint = int(mystring)
    return myint

while True:
    location = int(input()) # take user input
    tellNum(location) # send it to arduino
    var = hear() # listen to arduino
    print(var) #print what arduino sent