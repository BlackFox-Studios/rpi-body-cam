"""Module which holds PiCamera and PIR Sensor configurations."""

# Lines 5-7 import necessary Python libraries

import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep, asctime

# Lines 11-12 define variables for motion-detecting PIR sensor.

pir_sensor = 11
current_state = 0

# Lines 16-17 configure the RPi's breadboard

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pir_sensor, GPIO.IN)

# Lines below are responsible for running the motion-detecting PIR sensor and
# triggering the camera to record video if motion is detected. The script below
# will continuously execute until 'Ctrl+C' is pressed on the user's keyboard.

try:
    while True:
        sleep(0.1)
        current_state = GPIO.input(pir_sensor)
        if current_state == 1:
            with PiCamera() as camera:
                camera.start_preview()
                camera.annotate_text = 'Recording triggered by motion: {}'.format(asctime())
                camera.start_recording('/home/pi/Desktop/motion_detector_test.h264')
                sleep(10)
                camera.stop_recording()
                camera.stop_preview()
except(KeyboardInterrupt):
    print('Monitoring process: terminated.')
    GPIO.cleanup()
