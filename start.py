import serial
import time
import RPi.GPIO as GPIO

ser = serial.Serial(
	port='/dev/ttyAMA0',
	baudrate=9600,
	parity=serial.PARITY_ODD,
	stopbits=serial.STOPBITS_TWO,
	bytesize=serial.SEVENBITS
)

ser.reset_input_buffer()
ser.write("AT" + '\r\n')
time.sleep(2)

if ser.inWaiting() == 0:
    print "Module isn't started yet"

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(25, GPIO.OUT)
    GPIO.output(25, 1)
    time.sleep(2)
    GPIO.output(25, 0)
    time.sleep(2)

ser.reset_input_buffer()
ser.write("AT" + '\r\n')
time.sleep(2)

if ser.inWaiting() >= 0:
    print "Module started successfully"
    
