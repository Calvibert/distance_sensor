import RPi.GPIO as GPIO
import time

class DistanceSensor:

    def setup(self):
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)

        self.TRIG = 23
        self.ECHO = 24
        GPIO.setup(self.TRIG, GPIO.OUT)
        GPIO.setup(self.ECHO, GPIO.IN)

    def calculate_distance(self):
        GPIO.output(self.TRIG, False)
        print "Waiting For Sensor To Settle..."
        time.sleep(2)

        print 'Measuring distance...'

        GPIO.output(self.TRIG, True)
        time.sleep(0.00001)
        GPIO.output(self.TRIG, False)

        while GPIO.input(self.ECHO) == 0:
            pulse_start = time.time()

        while GPIO.input(self.ECHO)==1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        pulse_duration = pulse_duration / 2 # one-way trip only
        speed_of_sound = 343 # at sea level, in m/s
        #speed_of_sound = speed_of_sound * 100 # cm/s
        distance = speed_of_sound * pulse_duration

        print 'Distance: ',distance,' meters'
        return distance

    def close(self):
        GPIO.cleanup()
        print 'Exiting...'