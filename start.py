import serial
import time
import sys
import os
import RPi.GPIO as GPIO

from pathlib import Path

def start_module():
    #os.system("poff rnet")

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

        ser.flush()

        ser.close()

        #os.system("pon rnet")

def install_system():
    serial_port_s0 = Path("/dev/ttyS0")
    serial_port_ama0 = Path("/dev/ttyAMA0")
    if serial_port_s0.exists():
        print("Serial Port configured to /dev/ttyS0")
        serial_port = "/dev/ttyS0"
    elif serial_port_ama0.exists():
        print("Serial Port configured to /dev/ttyAMA0")
        serial_port = "/dev/ttyAMA0"
    else:
        print("Found no Serial port, please make sure to activate the Serial Port in raspi-config")

    apn = raw_input('Enter your APN: ')

    config =   ( "connect \"/usr/sbin/chat -v -f /etc/chatscripts/gprs -T " + str(apn) + "\"\n"
                "" + serial_port + "\n"
                "115200\n"
                "noipdefault\n"
                "usepeerdns\n"
                "defaultroute\n"
                "replacedefaultroute\n"
                "persist\n"
                "noauth\n"
                "nocrtscts\n"
                "local\n" )

    rnet_file = open("/etc/ppp/peers/rnet", "w")
    rnet_file.write(config)
    rnet_file.close()

    cron_file = open("/var/spool/cron/crontabs/root", "a").write("\n" + "@reboot python /opt/cellular_hat_installer/start.py start" + "\n")

if sys.argv[1] == "start":
    start_module()
elif sys.argv[1] == "install":
    install_system()


