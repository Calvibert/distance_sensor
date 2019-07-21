from distance_sensor import get_distance
from csv_ext import to_csv


try:
    while True:
        distance = get_distance()
        to_csv(distance)
except KeyboardInterrupt:
    print('interrupted!')