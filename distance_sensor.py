import RPi.GPIO as GPIO
import time

def get_distance():
    GPIO.setmode(GPIO.BCM)

    TRIG = 23
    ECHO = 24
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)

    GPIO.output(TRIG, False)
    print "Waiting For Sensor To Settle..."
    time.sleep(2)

    print 'Measuring distance...'

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    pulse_duration = pulse_duration / 2 # one-way trip only
    speed_of_sound = 343 # at sea level, in m/s
    #speed_of_sound = speed_of_sound * 100 # cm/s
    distance = speed_of_sound * pulse_duration

    print 'Distance: ',distance,' meters'

    GPIO.cleanup()
    print 'Exiting...'
    return distance
