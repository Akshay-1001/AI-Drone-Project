from djitellopy import tello
from time import sleep

# create an instance of the Tello class
my_drone = tello.Tello()

my_drone.connect()

print(my_drone.get_battery())

my_drone.takeoff()

my_drone.send_rc_control(50, 0, 0, 0)

sleep(2)