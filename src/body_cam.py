"""Module which holds PiCamera and PIR Sensor configurations."""

# Lines 5-7 import necessary Python libraries

import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep, asctime

button = 6
led = 18

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN)

# Lines below are responsible for running the motion-detecting PIR sensor and
# triggering the camera to record video if motion is detected. The script below
# will continuously execute until 'Ctrl+C' is pressed on the user's keyboard.

try:
    while True:
        if GPIO.input(button):
            sleep(1)
            print('Button has been pressed.')
            is_recording = 1
            GPIO.output(led, GPIO.HIGH)
            with PiCamera() as camera:
                camera.annotate_text = 'Recording triggered by button: {}'.format(asctime())
                print('Recording about to begin.')
                camera.start_recording('/home/pi/Desktop/testVid.h264')
                while is_recording:
                    if GPIO.input(button):
                        sleep(1)
                        is_recording = 0
                print('Button has been pressed again, recording is about to stop.')
                camera.stop_recording()
                GPIO.output(led, GPIO.LOW)
except(KeyboardInterrupt):
    print('Monitoring process: terminated.')
    GPIO.cleanup()
