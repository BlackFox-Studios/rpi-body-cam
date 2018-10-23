"""Module which holds PiCamera configurations."""

"""."""

import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep, asctime

pir_sensor = 11
current_state = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pir_sensor, GPIO.IN)

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

