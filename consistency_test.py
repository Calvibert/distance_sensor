from .distance_sensor import DistanceSensor
from csv_ext import to_csv

sensor = DistanceSensor()
sensor.setup()
try:
    while True:
        distance = sensor.calculate_distance()
        to_csv(distance)
except KeyboardInterrupt:
    sensor.close()
    print('interrupted!')