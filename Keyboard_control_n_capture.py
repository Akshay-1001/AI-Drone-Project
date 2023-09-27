from djitellopy import tello
import KeyPress_Module as kp
from time import sleep
import cv2

kp.init()
my_drone = tello.Tello()
my_drone.connect()
print(my_drone.get_battery())

my_drone.streamon()

global img

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 30
    if kp.getKey("LEFT"):
        lr = -speed
    elif kp.getKey("RIGHT"):
        lr = speed
    if kp.getKey("UP"):
        fb = speed
    elif kp.getKey("DOWN"):
        fb = -speed
    if kp.getKey("a"):
        yv = -speed
    elif kp.getKey("d"):
        yv = speed
    if kp.getKey("w"):
        ud = speed
    elif kp.getKey("s"):
        ud = -speed
    if kp.getKey("e"):
        my_drone.takeoff()
    if kp.getKey("q"):
        my_drone.land()
        sleep(3)
    return [lr, fb, ud, yv]

while True:
    vals = getKeyboardInput()
    my_drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)
    img = my_drone.get_frame_read().frame
    img = cv2.resize(img, (480, 240))
